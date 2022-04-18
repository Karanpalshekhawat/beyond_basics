"""
Sending email example
"""

import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASS = os.environ.get('EMAIL_PASS')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()  # identifies ourself with the mail server that we are using
    smtp.starttls()  # encrypted
    smtp.ehlo()  # identifies ourself again

    smtp.login(EMAIL_ADDRESS, EMAIL_PASS)

    subject = " What the status of lunch?"
    body = "How about lunch on next monday"

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, 'karanpal609@gmail.com', msg)
