from email.mime.text import MIMEText
import smtplib


def send_email(email, height):
    from_email="jmarc7862@gmail.com"
    from_pwd="Jmarc7862!"
    to_email=email

    subject="Height data"
    message ="Hey there, your height is <strong>%s</strong>. POING" % height

    msg = MIMEText(message,'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_pwd)
    gmail.send_message(msg)
