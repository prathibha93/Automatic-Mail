
import random
import smtplib
import datetime as dt
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch credentials and recipient from environment
my_email = os.getenv("MY_EMAIL")
password1 = os.getenv("EMAIL_PASS")
receiver_email = os.getenv("RECEIVER_EMAIL")

he = []

# Read quotes from file
with open("cs.txt", mode="r", encoding="utf-8") as file:
    f = file.readlines()
    for i in f:
        e = i.strip()
        he.append(e)

quote = random.choice(he)

# Get current weekday
current = dt.datetime.now()
h = current.weekday()

# Send email only if it's Saturday (weekday 5)
if h == 5:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password1)
        connection.sendmail(from_addr=my_email,
                            to_addrs=receiver_email,
                            msg=quote.encode('utf-8'))
