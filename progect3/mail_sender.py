import os
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(email, subject, text):
    addr_from = os.getenv('FROM')
    password = os.getenv('PASSWORD')

    msg = MIMEMultipart()
    msg['From'] = addr_from
    msg['To'] = email
    msg['Subject'] = subject
    body = text
    msg.attach(MIMEText(body, 'plain'))
    # приклепляем к серверу

    server = smtplib.SMTP_SSL(os.getenv('HOST'), os.getenv('POST'))
    server.login(addr_from, password)
    server.send_message(msg)
    server.quit()
    return True
