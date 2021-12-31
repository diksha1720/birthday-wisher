import datetime as dt
import smtplib
import pandas as pd
import random


def send_mail(msg, email):
    my_email = "testmail5290@gmail.com"
    my_pass = "test1234$$$"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, my_pass)
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject: Happy Birthday!!\n\n{msg}")


def create_mail(name, email):
    num = random.randint(1, 3)
    with open(f"letter_templates/letter_{num}.txt", "r") as letter:
        msg = letter.read()
        msg = msg.replace('[NAME]', name)
        send_mail(msg, email)


def check_date(day, month):
    data = pd.read_csv("birthdays.csv")
    data_list = data.to_dict(orient="records")
    for people_info in data_list:
        if people_info["month"] == month and people_info["day"] == day:
            create_mail(people_info["name"], people_info["email"])


now = dt.datetime.now()
date = now.day
month = now.month
check_date(date, month)



