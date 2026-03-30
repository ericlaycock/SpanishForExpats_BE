"""Email service for password reset via Gmail SMTP."""

import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.config import settings

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
