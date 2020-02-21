import logging
import os

import sendgrid
from sendgrid.helpers.mail import *


def send_mail(subject, content):
    if os.environ.get('SENDGRID_API_KEY') is None:
        logging.warning("Skipped sending mail... Set 'SENDGRID_API_KEY' env variable to send mail")
        return

    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("heroku-stackoverflow-fanatic-badge@heroku.com")
    to_email = Email(os.environ.get('STACK_OVERFLOW_EMAIL'))
    content = Content("text/plain", content)
    body = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=body.get())

    logging.debug(response.status_code)
    logging.debug(response.body)
    logging.debug(response.headers)
