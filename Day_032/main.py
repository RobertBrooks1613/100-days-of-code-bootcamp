import random
import datetime as dt
import smtplib
from tkinter import simpledialog

import pandas

now = dt.datetime.now()
year = now.year
month = now.month
week_day = now.day
subject = ""
body = ""
selected_name = ""

testy_boy = pandas.read_csv(filepath_or_buffer="birth_day.csv")
testy_boy.set_index('name', inplace=True)
testy_boy_dict = testy_boy.to_dict(orient='index')

birth_day = dt.datetime(month=2, day=25,year=1991)


email = "yukitori1613@gmail.com"        # simpledialog.askstring(title="Email", prompt="Enter your email: ")
password = "nrscawoemrzpxzuv"          # simpledialog.askstring(title="Password", prompt="Enter your password", show='*')
send_email_to = '' # simpledialog.askstring(title="Email", prompt="Enter the email you want to send to: ")

def check_birth_day():
    global selected_name
    for person,info in testy_boy_dict.items():
        day_ = info['day']
        month_ = info['month']
        if day_ == week_day and month_ == month:
            selected_name = person
            return True
    else:
        return False


def birthday_prep():
    global selected_name,send_email_to,subject,body
    send_email_to = selected_name
    subject = "Happy BirthDay!!"
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as ready:
        read_this = ready.read()
        body = read_this.replace("[NAME]",selected_name)
    if testy_boy_dict[selected_name]:
        send_email_to = testy_boy_dict[selected_name]['email']
    send_mail()


def quote_of_the_day():
    global subject,body,send_email_to
    quote_list = []
    check_week_day = now.weekday()
    if check_week_day == 0:
        for person,info in testy_boy_dict.items():
            send_email_to = info['email']
            with open("quotes.txt", "r") as reader:
                lines = reader.readlines()
                for line in lines:
                    quote_list.append(line.strip())
            subject = "Happy Monday! Here is your quote of the day!"
            body = random.choice(quote_list)
            print(person)
            print(body)
            send_mail()


def send_mail():
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=send_email_to,
                msg=f"Subject:{subject}\n\n{body}"
            )
            print("email sent")
    except (smtplib.SMTPAuthenticationError, smtplib.SMTPException, ConnectionError) as e:
        import tkinter.messagebox as messagebox; messagebox.showerror(title="Error", message=f"Error sending email: {e}")


if check_birth_day:
    birthday_prep()

quote_of_the_day()
