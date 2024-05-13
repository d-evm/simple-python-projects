import datetime as dt
import smtplib
import random as r
import pandas as pd

my_email = MY_EMAIL
password = PASSWORD

today = dt.datetime.today()

df = pd.read_csv("birthdays.csv")

birth_month = df["month"]
birth_day = df["day"]

is_birthday = (birth_day == today.day) & (birth_month == today.month)

if is_birthday.any():
    birthday_people = df[is_birthday]

    for _, row in birthday_people.iterrows():
        name = row["name"]
        email = row["email"]

        num = r.randint(1, 3)

        with open(file=f"letter_templates\letter_{num}.txt", mode="r") as file:
            template = file.read()

        birthday_wish = template.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(from_addr=my_email, to_addrs=email,
                                msg=f"Subject: Birthday wishes!\n\n{birthday_wish}")
