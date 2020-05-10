import smtplib

#spoof_email = "support@facebook.com"
sender_email = "essahcrypto@gmail.com"
receiver_email = "jurgenwo81@gmail.com"

password = "#z2FE#Hj7J9J"

message = """From: Facebook <support@facebook.com>
To: Jurgen Wolf <jurgenwo81@gmail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: Security warning

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login(sender_email, password)
print('login succesfull')

server.sendmail(sender_email, receiver_email, message)
print("your email has been sent to", receiver_email)
