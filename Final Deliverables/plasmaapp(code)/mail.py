import sendgrid
import os
from sendgrid.helpers.mail import *


def register_notify(email):
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("sbarath786@gmail.com")
    to_email = To(email)
    subject = "PlasmaApp - Registration"
    content = Content("text/plain", "Registration for opening an account was successfully completed. Now, you can login with your credentials.")
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)



def apply_notify(email):
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("sbarath786@gmail.com")
    to_email = To(email)
    subject = "Plasma Donation"
    content = Content("text/plain","Your application for donation of plasma was successfully done. You will get notified once a matched request found...")
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)



def request_notify(email):
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("sbarath786@gmail.com")
    to_email = To(email)
    subject = "Plasma Request"
    content = Content("text/plain", "Your request for needed plasma was succcessfully submitted. A perfect matched dono will contact you soon...")
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)