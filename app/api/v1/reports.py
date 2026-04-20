import logging

from fastapi import APIRouter, BackgroundTasks, Depends, status
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.database import get_db
from app.models import User, UserReport
from app.schemas import UserReportCreate, UserReportResponse
from app.services.email_service import send_report_notification

router = APIRouter()
logger = logging.getLogger(__name__)


def _safe_notify(report, reporter_email, recipients):
    """Call send_report_notification and swallow any exception.

    Defense-in-depth: send_report_notification is already expected to return
    False on failure rather than raise, but background tasks must never
    surface errors back to the client, so we guard here too.
    """
    try:
        send_report_notification(report, reporter_email, recipients)
    except Exception as e:
        logger.error(
            f"[Reports] Admin notification task raised for report {report.id}: {e}"
        )


@router.post(
    "",
    response_model=UserReportResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_report(
    payload: UserReportCreate,
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> UserReportResponse:
    """Persist a user-submitted report and notify admins asynchronously.

    The 201 response does not wait on SMTP — admin notification runs as a
    background task and must not fail the request if Gmail is misconfigured
    or unreachable.
    """
    report = UserReport(
        user_id=current_user.id,
        category=payload.category,
        description=payload.description,
        context=payload.context,
    )
    db.add(report)
    db.commit()
    db.refresh(report)

    admin_emails = [
        email
        for (email,) in db.query(User.email).filter(User.is_admin.is_(True)).all()
        if email
    ]

    if not admin_emails:
        logger.warning(
            f"[Reports] No admin users configured; skipping email for report {report.id}"
        )
    else:
        logger.info(
            f"[Reports] Scheduling admin notification for report {report.id} "
            f"to {len(admin_emails)} admin(s)"
        )
        background_tasks.add_task(
            _safe_notify,
            report,
            current_user.email,
            admin_emails,
        )

    return report
