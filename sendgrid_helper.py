import sendgrid
import os
from sendgrid.helpers.mail import *


def send_mail(subject, content):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("heroku-stackoverflow-fanatic-badge@heroku.com")
    to_email = Email(os.environ.get('STACK_OVERFLOW_EMAIL'))
    content = Content("text/plain", content)
    body = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=body.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
