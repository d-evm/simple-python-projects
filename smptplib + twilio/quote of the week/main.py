import smtplib
import datetime as dt
import random as r

my_email = MY_EMAIL
password = PASSWORD

now = dt.datetime.now()
if now.weekday() == 0:
    with open(file="quotes.txt", mode="r") as quotes:
        all_quotes = quotes.readlines()

    quote = r.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=RECIEVER_EMAIL,
                            msg=f"Subject: Quote of the week!\n\n{quote}")
