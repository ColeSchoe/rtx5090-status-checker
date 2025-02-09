import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
 
def send_message(message):
    # Start server, set connection to tls mode, log in, and send message
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(os.getenv("EMAIL"), os.getenv("APP_PW"))
    server.sendmail(os.getenv("EMAIL"), os.getenv("EMAIL"), message)
    server.quit()
 
if __name__ == "__main__":
    send_message("Hi from me again, this should be important!")