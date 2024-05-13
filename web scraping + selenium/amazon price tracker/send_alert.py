import smtplib
import datetime as dt
from twilio.rest import Client

my_email = MY_EMAIL
password = PASSWORD

account_sid = YOUR_ACC_SID
auth_token = YOUR_AUTH_TOKEN


class SendAlert:
    def __init__(self, url, price) -> None:
        self.url = url
        self.price = price
        self.alert_msg = f'''
Hurray! The price alert you set for your product is activated. 
It is currently priced at Rs.{price} (as of IST {dt.datetime.now()}).

The price might increase, so why wait? BUY NOW
{url}
'''
        self.send_mail()
        self.send_sms()

    def send_mail(self):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(from_addr=my_email, to_addrs=RECEIVER_EMAIL,
                                msg=f"Subject: PRICE ALERT!!!\n\n{self.alert_msg}")

    def send_sms(self):
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_=YOUR_TWILIO_NUMBER,
            body=self.alert_msg,
            to=RECEIVER_NUMBER
        )
