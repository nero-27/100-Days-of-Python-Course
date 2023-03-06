import datetime as dt
import random
import smtplib
import pandas

##################### Extra Hard Starting Project ######################
MY_EMAIL = 'richap2798@gmail.com'
PASSWORD = 'bqruauhedbjsrfqr'
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
today_date = today.day
today_month = today.month
today_tuple = (today_month, today_date)

data = pandas.read_csv('birthdays.csv')
birthday_dict = {
    (data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()
}
print(birthday_dict)
print(today_tuple)

#
if today_tuple in birthday_dict:
    file = f"letter_templates/letter_{random.randint(1,3)}.txt"
    name = birthday_dict[today_tuple]['name']
    email = birthday_dict[today_tuple]['email']

    with open(file) as letter_file:
        contents = letter_file.read()
        message = contents.replace("[NAME]", name)
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f'subject: HAPPY BIRTHDAY {name}!!! \n\n {message}'
            )




# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.





