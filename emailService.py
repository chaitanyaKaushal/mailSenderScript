# -------------------------------- Refer to README first before copying and pasting my script----------------------------------------------
# email would be sent to any machine having smtp,esmtp demon client installed
import smtplib as sm
# smtp is an email transfer protocol

# server has smtp ssl , smtp server-address and port no
server = sm.SMTP_SSL("smtp.gmail.com", 465)  # to check settings for gmail
# smtp.gmail.com is the smtp server address for gmail service

server.login("your mail id comes here", "your password comes here")
# sender , reciever, message, subject not considered
server.sendmail("sender mail id",
                "reciever mail id", "messsage")
server.quit()
