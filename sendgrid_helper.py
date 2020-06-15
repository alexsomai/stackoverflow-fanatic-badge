import logging
import os

import sendgrid
from sendgrid.helpers.mail import *


def send_mail(subject, content):
    if os.environ.get('SENDGRID_API_KEY') is None:
        logging.warning("Skipped sending mail... Set 'SENDGRID_API_KEY' env variable to send mail")
        return

    message = Mail(
        from_email=os.environ.get('STACK_OVERFLOW_EMAIL'),
        to_emails=os.environ.get('STACK_OVERFLOW_EMAIL'),
        subject=subject,
        html_content=content
    )

    sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)

    logging.debug(response.status_code)
    logging.debug(response.body)
    logging.debug(response.headers)
