import requests
import smtplib
import os

EMAIL = os.environ.get("email")
PASSWORD = os.environ.get("password")
SUBJECT = "Motivational Morning Phrase"

def send_email(message):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=message)

def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    data = response.json()
    return data["quote"]

def get_message():
    quote = get_quote()
    return f"subject:{SUBJECT}\n\n{quote} - Ye West"

def main():
    message = get_message()
    send_email(message)


main()
