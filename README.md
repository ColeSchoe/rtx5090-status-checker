# rtx5090-status-checker
A series of Python scripts using Selenium to gather data on RTX 5090 websites from common US retailers. By creating an .env file and a phone number, email, and email account password as variables automatic notifications can be made via email and text when any RTX 5090 is found to be in stock.

# Getting Started
Have Python downloaded within your project directory and create a virtual enviornment  
<br>
Then, install all dependencies like so:  

>pip install -r requirements.txt

Create a .env file and create the following variables:
>EMAIL = "your-email-address"  
>APP_PW = "your-password" (this may need to be an app password if using gmail, google app password to get that set up)  
>PHONE_NUM = "your-phone-number"  

Now run the main program to have all scrapers running continuously:  

>python ./main.py
