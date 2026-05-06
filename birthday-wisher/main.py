##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import random
from datetime import datetime
import pandas
import smtplib


today = datetime.now()
today_tuple = (today.month, today.day)
MY_EMAIL = "yashita1018@gmail.com"
MY_PASSWORD = "1234Yashi0987"

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
       content = letter_file.read()
       new_content = content.replace("[NAME]",birthday_dict[today_tuple]["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="yashitag2907@yahoo.com",
            msg=f"Subject:Birthday Wish\n\n{new_content}"
        )








