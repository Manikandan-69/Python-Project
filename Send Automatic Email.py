import os
import random
import smtplib  

#smtplib is a built-in Python module used for sending emails using the Simple Mail Transfer Protocol (SMTP). 
# It allows you to connect to an email server, authenticate, and send messages.

"""
    SMTP Server Addresses for Common Email Providers
    Email Provider	SMTP Server	Port
    Gmail	smtp.gmail.com	587
    Outlook	smtp.office365.com	587
    Yahoo Mail	smtp.mail.yahoo.com	465
    Zoho Mail	smtp.zoho.com	465
"""

def automatic_email():
    user=input('Enter User Name: ')
    email=input('Enter Your Email: ')

    sender_mail = ''  #your email
    sender_password ='' #Use an app password for security

    subject= " "  # Email subject
    body=f"Dear {user},\n\n Welcome to the world of IT \n \n\Regards,\n Team Data Science "
    message= (f"Subject: {subject} \n\n {body}")
    
    try:
        s=smtplib.SMTP('smtp.gmail.com',587) #Based of send Email you have to change the SMTP server  and port . 
        s.starttls() #upgarde to secure connection
        s.login(sender_mail,sender_password)

        s.sendmail(sender_mail, email, message)  #from,to,message
        print("Email Sent!")

        s.quit()

    except Exception as e:
        print(f'Error: {e}')


automatic_email()