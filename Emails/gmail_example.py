"""
Sending email example
"""

import os
import imghdr
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

    # smtp.sendmail(EMAIL_ADDRESS, 'karanpal609@gmail.com', msg)

"""Much better approach"""
msg = EmailMessage()
msg['Subject'] = "What the status of lunch?"
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'karanpal609@gmail.com'
msg.set_content("How about lunch on next monday")

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_3:
    smtp_3.login(EMAIL_ADDRESS, EMAIL_PASS)
    smtp_3.send_message(msg)

"""Email Attachment"""

# with ('image.png', 'rd') as f:
#     file_data = f.read()
#     file_type = imghdr.what(f.name)  # help to find out the file type
#     file_name = f.name
#
# msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
