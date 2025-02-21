import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "pyforeveryone@gmail.com"
    password = os.getenv("MYPASSWORD")
    receiver = "pyforeveryone@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


send_email("hi, ghoulam")