import smtplib
import datetime as dt
import random
my_email = "coderslif@gmail.com"
password = "jyfqe2-faskad-nAdjuk"


current_date = dt.datetime.now()
current_weekday = current_date.weekday()

if current_weekday == 1:
    with open("quotes.txt") as data:
        quotes_list = data.readlines()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="denis.poloczek.97@gmail.com",
            msg=f"Subject: Monday's motivational quotes \n\n {random.choice(quotes_list)}"

        )
