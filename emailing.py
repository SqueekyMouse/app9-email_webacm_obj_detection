import os
# commit: email section Sec36

host='smtp.gmail.com'
port=465
username='appuser565@gmail.com'
password=os.getenv('APP_M_PASSWORD')
receiver='appuser565@gmail.com'

def send_email():
    print('Email was sent')