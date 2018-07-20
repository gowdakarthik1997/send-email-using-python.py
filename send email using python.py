import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("email address","password")
server.sendmail("email address","reciver email address",message("hello")
