import smtplib as sm
# email would be sent to any machine having smtp,esmtp demon client installed
# smtp is an email transfer protocol
# ----------
# server has smtp ssl , smtp server-address and port no
server = sm.SMTP_SSL("smtp.gmail.com", 465)  # to check settings for gmail
# smtp.gmail.com is the smtp server address for gmail service
server.login("your mail comes here", "your password comes here")
# sender , reciever, message, subject not considered
server.sendmail("sender mail",
                "reciever mail", "messsage")
server.quit()

# For SMTP authentication to be successful ->
# if 2 step verification is available then generate an app password in your google account settings
# if you disable 2 step verification, you should give access to Less Secure mail in your google account settings
