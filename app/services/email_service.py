"""Email service for password reset via Gmail SMTP."""

import smtplib
import logging
import json
from html import escape
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import TYPE_CHECKING, Optional

from app.config import settings

if TYPE_CHECKING:
    from app.models import UserReport

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
