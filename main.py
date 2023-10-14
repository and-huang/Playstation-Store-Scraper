import requests
from bs4 import BeautifulSoup
import time
import random
import smtplib, ssl
from datetime import date


URL = "https://www.playstation.com/en-us/games/insert-title-of-game-here/" #Modify URL with game title
response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")
time.sleep(random.randint(2, 6))
if soup.find("span", attrs={"class": "psw-t-title-m psw-m-r-4"}) == None:
	price = soup.find("span", attrs={"class": "psw-t-title-m"})
else:
	price = soup.find("span", attrs={"class": "psw-t-title-m psw-m-r-4"})
time.sleep(random.randint(2, 6))
title = soup.find("h1", attrs={"class": "game-title"})

path = "" #replace with absolute path to your text file storing the lowest price

lowestPrice = open(path, "r")
currLowest = lowestPrice.read()
currLowestFloat = float(currLowest[1:7])
if float(price.text[1:7]) < currLowestFloat: #You only get emailed if the price is lower
    newLowest = open(path, "w")
    newLowest.write(price.text)

    port = 000 #Replace with port
    smtp_server = "" #I used smtp.gmail.com
    sender_email = "" #Replace with your email
    receiver_email = "" #Replace with recipient email
    password = "" #For Gmail users, you have to enable 2FA and request an app password in settings, separate from your normal Gmail password
    message = f"""\
    Subject: Price of {title.text}
    
    As of {date.today()}, the price of {title.text} is {price.text}."""
    
    #Establish client-server encryption
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    newLowest.close()
lowestPrice.close()
#For Windows users, you can automate/schedule this file using Task Scheduler
#For Mac users, you can automate/schedule this file using Apple's Automator
