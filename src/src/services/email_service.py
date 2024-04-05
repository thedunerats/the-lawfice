# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import base64
import logging
import os
from email_validator import validate_email, EmailSyntaxError
from email_validator.exceptions_types import EmailUndeliverableError
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

logger = logging.getLogger(__name__)


def send_email(from_email, to_emails, subject, content):
    other_thing = os.getenv('SENDGRID_KEY')
    message = Mail(
        from_email=from_email,
        to_emails=to_emails,
        subject=subject,
        html_content=content)
    try:
        sg = SendGridAPIClient(other_thing)
        response = sg.send(message)
        logging.info(response.status_code)
        logging.info(response.body)
        logging.info(response.headers)
    except Exception as e:
        logger.error(e)
    return response


def is_valid_email(email: str) -> bool:
    try:
        is_valid = validate_email(email).normalized
    except (EmailSyntaxError, EmailUndeliverableError) as error:
        logger.error(error)
        return False
    return is_valid == email
