import smtplib
import ssl
import os

host = "smtp.gmail.com"
port = 465

username = "zigouris.konstantinos@gmail.com"
password = os.getenv("portfolio_pass")

receiver = "zigouris.konstantinos@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hi!
how are you?
Bye!
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
