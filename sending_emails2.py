import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(recipients, text):
    sender_email = "xamchy12@gmail.com"
    sender_password = "qvdx akpu mnlw qiyh" #Use Google App password

    
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls

    # Create a secure SSL context
    context = smtplib.SMTP(smtp_server, port)
    try:
        # Try to log in to server and send email
        context.ehlo()
        context.starttls() # Secure the connection
        context.ehlo()
        context.login(sender_email, sender_password)
        
        for recipient in recipients:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient
            msg['Subject'] = "Your Subject Here"
            msg.attach(MIMEText(text, 'plain'))

            # Send the email
            context.sendmail(sender_email, recipient, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        context.quit()

# Example usage
        """""
recipients = ["iftekhar.chowdhury05@northsouth.edu", "xamchy99@gmail.com"]
text = "Hello, this is a test message."
send_email(recipients, text)
"""