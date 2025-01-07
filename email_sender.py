import smtplib,ssl


def send_email(sender,message):
    host = 'smtp.gmail.com'
    port = 465
    # sender = "sumit.dangi19@gmail.com"
    password = "zcgyfzrahoxthtns"
    receiver = "sumit.dangi19@gmail.com"
    context = ssl.create_default_context()
    message = f"""\
Subject: Hi!

From: {sender}
{message}
"""
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)

