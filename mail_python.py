import smtplib
from email.message import EmailMessage

msg=EmailMessage()
msg['subject']='something'
msg['From']='USER'
msg['To']='mention mail'
msg.set_content("Test Email")

with open('output.txt') as myfile:
    data=myfile.read()
    msg.set_content(data)

''''
write something here

''''
server=smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login("mention mail server credentials"," ")
server.send_message(msg)
server.quit()
