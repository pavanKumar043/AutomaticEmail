import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import time

sender_email= 'sayannagari13@gmail.com'
sender_pass='pjth iwfg ptok jwta'
receiver_email='pavankumarsayannagari13@gmail.com'

smtp_server='smtp.gmail.com'
smtp_port=587

def send_email():
    msg= MIMEMultipart()
    msg['From']=sender_email
    msg['To']=receiver_email
    msg['Subject']='Automated Email from Pavan'
    '''message="pava"
    for i in range(20):
        message+='a'
    '''
    body='Hello!, Good Evening '+str(datetime.now())
    msg.attach(MIMEText(body, 'plain'))
    try:
        server=smtplib.SMTP(smtp_server,smtp_port)
        server.starttls()
        server.login(sender_email,sender_pass)
        server.send_message(msg)
    except Exception as e:
        print(f"Error occurred {e}")
    finally: 
        server.quit()

interval=3600 

while True:
    send_email()
    print(f"Email sent at {datetime.now()}")
    time.sleep(interval)




