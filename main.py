import requests
from bs4 import BeautifulSoup
import time
import random
import smtplib, ssl
from datetime import date


URL = "https://www.playstation.com/en-us/games/insert-title-of-game-here/" #Modify URL with game title
response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")
time.sleep(random.randint(2, 6)) #This makes it slightly less likely that we will be detected by some security protocols
price = soup.find("span", attrs={"class": "psw-t-title-m psw-m-r-4"})
time.sleep(random.randint(2, 6))
title = soup.find("h1", attrs={"class": "game-title"})

port = 000 #Replace with port
smtp_server = "" #I used smtp.gmail.com
sender_email = "" #Replace with your email
receiver_email = "" #Replace with recipient email
password = "" #For Gmail users, you have to enable 2FA and request an app password in settings, separate from your normal Gmail password
message = f"""\
Subject: Price of PS4 game

As of {date.today()}, the price of {title.text} is {price.text}."""

#Establish client-server encryption
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

#For Windows users, you can automate/schedule this file using Task Scheduler
#For Mac users, you can automate/schedule this file using Apple's Automator
