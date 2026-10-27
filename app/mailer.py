"""Email through the Brevo API. Never raises: a mail problem must not lose an enquiry."""
import base64
import logging
import os

import requests
from django.conf import settings

log = logging.getLogger(__name__)


def send_brevo_email(to_email, subject, text, attachment=None, attachment_name=None, reply_to=None):
    api_key = os.environ.get("BREVO_API_KEY")
    if not api_key:
        log.warning("BREVO_API_KEY is not set; email not sent: %s", subject)
        return False
    data = {
        "sender": {"email": settings.SENDER_EMAIL, "name": "Neminath Wood Industry Pvt Ltd"},
        "to": [{"email": to_email}],
        "subject": subject,
        "textContent": text,
    }
    if reply_to:
        data["replyTo"] = {"email": reply_to}
    if attachment is not None:
        data["attachment"] = [{
            "content": base64.b64encode(attachment).decode(),
            "name": attachment_name or "attachment",
        }]
    try:
        r = requests.post(
            "https://api.brevo.com/v3/smtp/email",
            json=data,
            headers={"api-key": api_key, "Content-Type": "application/json"},
            timeout=10,
        )
        if r.status_code >= 300:
            log.error("Brevo error %s: %s", r.status_code, r.text[:300])
            return False
        return True
    except requests.RequestException as exc:
        log.error("Brevo request failed: %s", exc)
        return False
