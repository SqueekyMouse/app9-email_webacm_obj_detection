import smtplib
import os
from email.message import EmailMessage # to create email obj
import imghdr #to get image metadata
# commit: done email module to send attachment and mail Sec37

SENDER='appuser565@gmail.com'
PASSWORD=os.getenv('APP_M_PASSWORD')
RECEIVER='appuser565@gmail.com'

def send_email(image_path):
    email_message=EmailMessage() # to create email obj, its basically a dict
    email_message['Subject']='New customer showed up!'
    email_message.set_content('Hey, we just saw a new customer!')
    
    with open(image_path,'rb') as file:
        content=file.read()
    
    email_message.add_attachment(content,maintype='image',
                                 subtype=imghdr.what(None,content)) # get img type from the image metadata
    
    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER,PASSWORD)
    gmail.sendmail(SENDER,RECEIVER,email_message.as_string())
    gmail.quit()

if __name__=='__main__':
    send_email(image_path='images/image.png')