import smtplib
import datetime as dt
import random

def get_quote():
    with open("quotes.txt", "r") as f:
        quotes = f.readlines()
        num = random.randint(0, len(quotes)-1)
        quote_of_the_day = quotes[num]

    return quote_of_the_day

my_email = "pavankoushik2023@gmail.com"
password = "hosi todh pbir oawz"
now = dt.datetime.now()
weekday = now.weekday()

if weekday<8:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        my_quote = get_quote()
        msg = f"Subject:YOUR DAILY DOSE FOR THE DAY\n\n {my_quote}"
        connection.sendmail(
            from_addr=my_email,
            to_addrs="rojaramani6@gmail.com",
            msg=msg
        )






