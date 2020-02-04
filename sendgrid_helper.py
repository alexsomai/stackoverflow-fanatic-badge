import sendgrid
import os
from sendgrid.helpers.mail import *
import logging


def send_mail(subject, content):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("heroku-stackoverflow-fanatic-badge@heroku.com")
    to_email = Email(os.environ.get('STACK_OVERFLOW_EMAIL'))
    content = Content("text/plain", content)
    body = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=body.get())
    # Replaced print methods with relevant logging methods (logging.info)
    logging.basicConfig(level=logging.INFO)
    logging.info(response.status_code)
    logging.info(response.body)
    logging.info(response.headers)
