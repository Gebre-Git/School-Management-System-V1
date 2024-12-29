import smtplib


sender = "gabrellstem777@gmail.com"
receiver = "gabrellstem77@gmail.com"
password = "Gebre#$#777"
subject = "about python email test"
body = """python email test is very interesting part of the python
          automation.\n It is the test for that
       """
message = f'''From: Gabrell {sender}
              To: Receiver {receiver}
              subject: {subject}\n
              {body}
          '''
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError:
    print("unable to signin ")