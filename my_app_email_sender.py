from email.message import EmailMessage
from smtplib import SMTP_SSL
from os import getenv
import ssl


email_sender = getenv('ADDITIONAL_EMAIL')
email_receiver = getenv('ADMIN_EMAIL')
email_app_password = getenv('MY_APP_PASSWORD')

subject = 'Message is here'
body = """
Welcome to the Funland, Sonic!
"""

mail = EmailMessage()
mail['From'] = email_sender
mail['To'] = email_receiver
mail['Subject'] = subject
mail.set_content(body)

context = ssl.create_default_context()

with SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_app_password)
    smtp.sendmail(email_sender, email_receiver, mail.as_string())


