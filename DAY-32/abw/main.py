##################### Extra Hard Starting Project ######################
import pandas as pd
import smtplib
import datetime as dt
import random

# 1. Update the birthdays.csv-DONE


# 2. Check if today matches a birthday in the birthdays.csv
list_of_bd = pd.read_csv("birthdays.csv")
today = dt.datetime.now()
day = today.day
bd_days = list_of_bd["day"].tolist()
bd_names = list_of_bd["name"].tolist()
my_email = "pavankoushik2023@gmail.com"
password = "hosi todh pbir oawz"
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def get_random_message(name):
    search_text = "[NAME]"
    file_num = random.randint(1,3)
    file_name = fr"C:\Users\koush\PycharmProjects\days100code\DAY-32\abw\letter_templates\letter_{file_num}.txt"
    with open(file_name, "r") as f:
        data = f.read()
        my_msg = data.replace(search_text, name)

    return my_msg

# 4. Send the letter generated in step 3 to that person's email address.
for i in range(len(bd_days)):
    if int(bd_days[i]) == day:
        name = bd_names[i]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            my_msg = get_random_message(name)

            connection.sendmail(
                from_addr=my_email,
                to_addrs="rojaramani6@gmail.com",
                msg=my_msg
            )



