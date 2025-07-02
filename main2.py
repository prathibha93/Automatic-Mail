import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

my_email = os.getenv("MY_EMAIL")
password1 = os.getenv("EMAIL_PASS")
receiver_email = os.getenv("RECEIVER_EMAIL")

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password1)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=receiver_email,
        msg="Subject:Hello\n\nThis is the body"
    )


