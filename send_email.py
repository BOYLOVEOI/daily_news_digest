# Import statements
import os
import smtplib, ssl

# Creating the function, send_mail() to send news information to the user
def send_email(message):
    # Configuration settings
    host = "smtp.gmail.com"
    port = 465
    username = "plavoieportfolio@gmail.com"
    password = os.environ["PASSWORD"]
    context = ssl.create_default_context()

    # Email recipient settings
    receiver = "plavoieportfolio@gmail.com"


    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username, password)
        server.sendmail(from_addr=username, to_addrs=receiver, msg=message)