import smtplib as sm
# email would be sent to any machine having smtp,esmtp demon client installed
# smtp is an email transfer protocol
# ----------
# server has smtp ssl , smtp server-address and port no
server = sm.SMTP_SSL("smtp.gmail.com", 465)  # to check settings for gmail
# smtp.gmail.com is the smtp server address for gmail service
server.login("ckaushal2028@gmail.com", "buttercup@@34")
# sender , reciever, message, subject not considered
server.sendmail("ckaushal2028@gmail.com",
                "ckaushal_be18@thapar.edu", "Hello ! How are you")
server.quit()
# APP PASSWORD -> mbakyltbloqbxpqx
