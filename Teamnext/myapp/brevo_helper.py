import urllib.request
import urllib.error
import json
import os


def send_brevo_email(to_emails, subject, html_content, plain_text=None):
    """
    Send email via Brevo HTTP API (works on Render free plan).
    SMTP port 587 is blocked by Render, but HTTPS API works fine.
    
    to_emails: list of email strings e.g. ['user@example.com']
    subject: string
    html_content: HTML string
    plain_text: optional plain text fallback
    """
    api_key = os.environ.get("BREVO_API_KEY") or os.environ.get("EMAIL_HOST_PASSWORD")
    from_email = os.environ.get("DEFAULT_FROM_EMAIL", "otp@teamnexterp.com")
    from_name = "TeamNext ERP"

    if not api_key:
        raise Exception("BREVO_API_KEY not set in environment variables")

    payload = {
        "sender": {"name": from_name, "email": from_email},
        "to": [{"email": e} for e in to_emails],
        "subject": subject,
        "htmlContent": html_content,
    }
    if plain_text:
        payload["textContent"] = plain_text

    data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        "https://api.brevo.com/v3/smtp/email",
        data=data,
        headers={
            "accept": "application/json",
            "api-key": api_key,
            "content-type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        raise Exception(f"Brevo API error {e.code}: {error_body}")
    except Exception as e:
        raise Exception(f"Brevo send failed: {str(e)}")
