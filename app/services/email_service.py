"""Email service for password reset via Gmail SMTP."""

import smtplib
import logging
import json
from html import escape
from datetime import datetime, timezone
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
from typing import TYPE_CHECKING, Optional, Sequence
from zoneinfo import ZoneInfo

from app.config import settings

if TYPE_CHECKING:
    from app.models import Cohort, UserReport

logger = logging.getLogger(__name__)

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587


def send_reset_email(to_email: str, reset_url: str) -> bool:
    """Send a password reset email. Returns True on success."""
    if not settings.smtp_email or not settings.smtp_app_password:
        logger.error("[Email] SMTP not configured (SMTP_EMAIL / SMTP_APP_PASSWORD missing)")
        return False

    subject = "Reset your Spanish for Expats password"
    html = f"""
    <div style="font-family: sans-serif; max-width: 480px; margin: 0 auto; padding: 24px;">
        <h2 style="color: #28968C;">Password Reset</h2>
        <p>You requested a password reset for your Spanish for Expats account.</p>
        <p>Click the button below to set a new password. This link expires in 1 hour.</p>
        <a href="{reset_url}"
           style="display: inline-block; background: #28968C; color: white; padding: 12px 24px;
                  border-radius: 8px; text-decoration: none; font-weight: 600; margin: 16px 0;">
            Reset Password
        </a>
        <p style="color: #666; font-size: 14px;">If you didn't request this, you can safely ignore this email.</p>
        <p style="color: #999; font-size: 12px;">— Spanish for Expats</p>
    </div>
    """

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"Spanish for Expats <{settings.smtp_email}>"
    msg["To"] = to_email
    msg.attach(MIMEText(f"Reset your password: {reset_url}", "plain"))
    msg.attach(MIMEText(html, "html"))

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(settings.smtp_email, settings.smtp_app_password)
            server.send_message(msg)
        logger.info(f"[Email] Reset email sent to {to_email}")
        return True
    except Exception as e:
        logger.error(f"[Email] Failed to send to {to_email}: {e}")
        return False


def send_report_notification(
    report: "UserReport",
    reporter_email: Optional[str],
    recipients: list[str],
) -> bool:
    """Notify admins about a newly submitted user report.

    Must never raise: it runs in a FastAPI BackgroundTasks context and
    SMTP failures should not surface to the client. Returns True on success.
    """
    if not recipients:
        logger.warning(f"[Email] No recipients for report {report.id}, skipping")
        return False

    if not settings.smtp_email or not settings.smtp_app_password:
        logger.error(
            f"[Email] SMTP not configured; cannot notify admins about report {report.id}"
        )
        return False

    try:
        description_preview = (report.description or "")[:60]
        subject = f"[SFE Report] {report.category} — {description_preview}"

        reporter_label = reporter_email or "anonymous"
        context_json = json.dumps(report.context or {}, indent=2, default=str, sort_keys=True)
        created_at_iso = report.created_at.isoformat() if report.created_at else ""

        text_body = (
            f"New user report\n"
            f"ID: {report.id}\n"
            f"Category: {report.category}\n"
            f"Status: {report.status}\n"
            f"Created: {created_at_iso}\n"
            f"Reporter: {reporter_label}\n\n"
            f"Description:\n{report.description}\n\n"
            f"Context:\n{context_json}\n"
        )

        html_body = f"""
        <div style="font-family: sans-serif; max-width: 480px; margin: 0 auto; padding: 24px;">
            <h2 style="color: #28968C;">New User Report</h2>
            <p><strong>ID:</strong> {escape(str(report.id))}<br>
               <strong>Category:</strong> {escape(report.category)}<br>
               <strong>Status:</strong> {escape(report.status)}<br>
               <strong>Created:</strong> {escape(created_at_iso)}<br>
               <strong>Reporter:</strong> {escape(reporter_label)}</p>
            <h3 style="color: #28968C; font-size: 14px; margin-top: 20px;">Description</h3>
            <p style="white-space: pre-wrap;">{escape(report.description or "")}</p>
            <h3 style="color: #28968C; font-size: 14px; margin-top: 20px;">Context</h3>
            <pre style="background: #f5f5f5; padding: 12px; border-radius: 6px;
                        font-size: 12px; overflow-x: auto;">{escape(context_json)}</pre>
            <p style="color: #999; font-size: 12px;">— Spanish for Expats</p>
        </div>
        """

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = f"Spanish for Expats <{settings.smtp_email}>"
        msg["To"] = ", ".join(recipients)
        msg.attach(MIMEText(text_body, "plain"))
        msg.attach(MIMEText(html_body, "html"))

        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(settings.smtp_email, settings.smtp_app_password)
            server.send_message(msg)
        logger.info(
            f"[Email] Report notification sent for report {report.id} to {len(recipients)} admin(s)"
        )
        return True
    except Exception as e:
        logger.error(f"[Email] Failed to send report notification for report {report.id}: {e}")
        return False


def _format_session_line(start_utc: datetime, cohort_tz: str) -> tuple[str, str]:
    """Render a single session timestamp two ways:
    - primary: cohort timezone with explicit offset (e.g. 'Thu, May 7, 2026 · 10:00 AM Pacific Time (PDT, UTC−7)')
    - secondary: also shown in Eastern + UTC, so non-PT readers see at least two zones.
    """
    if start_utc.tzinfo is None:
        start_utc = start_utc.replace(tzinfo=timezone.utc)
    pt = start_utc.astimezone(ZoneInfo(cohort_tz))
    et = start_utc.astimezone(ZoneInfo("America/New_York"))
    utc = start_utc.astimezone(timezone.utc)

    pt_offset_hours = int(pt.utcoffset().total_seconds() // 3600)
    pt_offset = f"UTC{'+' if pt_offset_hours >= 0 else '−'}{abs(pt_offset_hours)}"
    pt_abbr = pt.strftime("%Z") or "PT"

    primary = (
        f"{pt.strftime('%A, %B %-d, %Y')} · "
        f"{pt.strftime('%-I:%M %p').lstrip('0')} Pacific Time ({pt_abbr}, {pt_offset})"
    )
    secondary = (
        f"Also: {et.strftime('%-I:%M %p').lstrip('0')} Eastern · "
        f"{utc.strftime('%H:%M')} UTC"
    )
    return primary, secondary


def send_cohort_confirmation(
    to_email: str,
    name: str,
    cohort: "Cohort",
    session_starts: Sequence[datetime],
    zoom_url: Optional[str],
    ics_payload: str,
) -> bool:
    """Send the post-registration confirmation email with all 3 session
    times (timezone overcommunicated), Zoom link, and a .ics attachment.
    Returns True on success.
    """
    if not settings.smtp_email or not settings.smtp_app_password:
        logger.error("[Email] SMTP not configured (SMTP_EMAIL / SMTP_APP_PASSWORD missing)")
        return False

    subject = f"You're in: {cohort.name} cohort confirmation"
    zoom_html = (
        f'<a href="{escape(zoom_url)}" style="color: #28968C; word-break: break-all;">{escape(zoom_url)}</a>'
        if zoom_url
        else '<em>(Zoom link will be sent before your first session.)</em>'
    )

    session_html_blocks: list[str] = []
    session_text_lines: list[str] = []
    for i, start in enumerate(session_starts, start=1):
        primary, secondary = _format_session_line(start, cohort.timezone)
        session_html_blocks.append(
            f"""
            <div style="border-left: 3px solid #28968C; padding: 10px 14px; margin: 10px 0; background: #f6fbfa;">
                <div style="font-weight: 600; color: #1f2937;">Session {i}</div>
                <div style="color: #1f2937; margin-top: 4px;">{escape(primary)}</div>
                <div style="color: #6b7280; font-size: 13px; margin-top: 2px;">{escape(secondary)}</div>
            </div>
            """
        )
        session_text_lines.append(f"Session {i}: {primary}\n  {secondary}")

    html = f"""
    <div style="font-family: sans-serif; max-width: 560px; margin: 0 auto; padding: 24px;">
        <h2 style="color: #28968C; margin-bottom: 8px;">You're registered, {escape(name)}!</h2>
        <p style="color: #374151;">You're confirmed for the <strong>{escape(cohort.name)}</strong> cohort.
        We meet for three 60-minute sessions on Zoom.</p>

        <h3 style="color: #28968C; font-size: 16px; margin-top: 24px;">Your sessions</h3>
        {''.join(session_html_blocks)}

        <h3 style="color: #28968C; font-size: 16px; margin-top: 24px;">Zoom link (same for all 3 sessions)</h3>
        <p>{zoom_html}</p>

        <p style="color: #6b7280; font-size: 13px; margin-top: 24px;">
            We've attached a calendar file (<code>spanish-cohort.ics</code>) with all three sessions —
            open it to add them to Google Calendar, Apple Calendar, or Outlook.
            All times above are shown in <strong>Pacific Time</strong> first; your calendar app
            will convert them to your local timezone automatically.
        </p>
        <p style="color: #9ca3af; font-size: 12px; margin-top: 24px;">— Spanish for Expats</p>
    </div>
    """

    text_body = (
        f"You're registered, {name}!\n\n"
        f"Cohort: {cohort.name}\n\n"
        + "\n\n".join(session_text_lines)
        + f"\n\nZoom link (same for all sessions): {zoom_url or 'TBD — will be sent before session 1'}\n\n"
        "All times are Pacific Time. Your calendar app will convert to your local zone.\n"
        "— Spanish for Expats\n"
    )

    # mixed = alternative (text+html) + attachment
    msg = MIMEMultipart("mixed")
    msg["Subject"] = subject
    msg["From"] = f"Spanish for Expats <{settings.smtp_email}>"
    msg["To"] = to_email

    body = MIMEMultipart("alternative")
    body.attach(MIMEText(text_body, "plain"))
    body.attach(MIMEText(html, "html"))
    msg.attach(body)

    ics_part = MIMEBase("text", "calendar", method="PUBLISH", name="spanish-cohort.ics")
    ics_part.set_payload(ics_payload)
    encoders.encode_base64(ics_part)
    ics_part.add_header(
        "Content-Disposition", "attachment", filename="spanish-cohort.ics"
    )
    msg.attach(ics_part)

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(settings.smtp_email, settings.smtp_app_password)
            server.send_message(msg)
        logger.info(f"[Email] Cohort confirmation sent to {to_email} for cohort {cohort.slug}")
        return True
    except Exception as e:
        logger.error(f"[Email] Failed to send cohort confirmation to {to_email}: {e}")
        return False
