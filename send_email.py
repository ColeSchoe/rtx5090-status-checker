import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(message):
    # Start server, set connection to tls mode, log in, and send message
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(os.getenv("EMAIL"), os.getenv("APP_PW"))
    
    server.sendmail(os.getenv("EMAIL"), os.getenv("EMAIL"), message)

    server.quit()
 
def send_message(message):
    # Start server, set connection to tls mode, log in, and send message
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(os.getenv("EMAIL"), os.getenv("APP_PW"))

    recipient = os.getenv("PHONE_NUM") + "@vtext.com"
    server.sendmail(os.getenv("EMAIL"), recipient, message)

    server.quit()
 
if __name__ == "__main__":
    send_email("Hi from me again, this should be a text!")