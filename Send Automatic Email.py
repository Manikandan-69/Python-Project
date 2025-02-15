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


"""
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Test Email with Attachment"
msg.set_content("Please find the attached file.")

# Attach a file
with open("sample.pdf", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename="sample.pdf")

# Send the email
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.send_message(msg)

print("Email sent with attachment!")

"""