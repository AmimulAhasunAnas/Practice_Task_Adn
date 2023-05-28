# -*- coding: utf-8 -*-
"""Mean,Median,Mode Using Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jsfLOjUU46KJeUdjO8bHezHecSfi4PHZ
"""

import pandas as pd
import numpy as np
from statistics import mean,median,mode,stdev
import scipy.stats as stats
import matplotlib.pyplot as plt

age = [5,10,12,15,13,20,25,30,32,35,43]

mean = mean(age)
print(mean)

median=median(age)
mode=mode(age)
print(median)
print(mode)

Zscores = stats.zscore(age)
print(Zscores)

plt.hist(age,bins='auto')
plt.title('Histogram of Age Bins')
plt.savefig("Histogram.png")
plt.show()

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders
import datetime
today = datetime.date.today()
# Email configuration
sender_email = 'anasamimulahasun@gmail.com'
sender_password = 'wbegxjinlzjmwfzt'
receiver_email = 'almehady@gmail.com'
bcc_email='anas180498@gmail.com'
date = datetime.datetime.now()
subject = "Histogram report of " + str(today)
message =  " Dear Sir, \n\n.I sent the attachmement of histrogram \n\n MD. Amimul Ahasun Anas\n Data Analyst\n"+" "+datetime.datetime.now().strftime("%H:%M:%S")

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Bcc'] = bcc_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))
# Attach the histogram.png file
with open('Histogram.png', 'rb') as file:
    image = MIMEImage(file.read(), name='Histogram.png')
    msg.attach(image)
# Connect to the SMTP server and send the email
with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(msg)