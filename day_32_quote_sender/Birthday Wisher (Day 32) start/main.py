import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

my_email = "richap2798@gmail.com"
password = "bqruauhedbjsrfqr"

quotes = []
weekdays = [0, 1, 2, 3, 4, 5, 6, 7]

if weekday in weekdays:
    with open('quotes.txt', 'r') as f:
        quotes = f.readlines()

    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="richie02227@gmail.com",
            msg=f"subject: Quote of the day!. \n\n .{random.choice(quotes)}")
