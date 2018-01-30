import sendgrid
import os
from sendgrid.helpers.mail import *


def send_mail():
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("app86550363@heroku.com")
    subject = "Hello World from the SendGrid Python Library!"
    to_email = Email("alexsomai30@gmail.com")
    content = Content("text/plain", "Hello, Email!")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


send_mail()
