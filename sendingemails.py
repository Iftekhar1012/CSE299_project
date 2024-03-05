import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_emails(emails, text):
    smtp_server = 'smtp.example.com'  
    smtp_port = 587 
    sender_email = 'your_email@example.com' 
    sender_password = 'your_password' 

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    for email in emails:
        msg = MIMEMultipart('alternative')
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = 'Subject of the Email'

        text_part = MIMEText(text, 'plain')
        msg.attach(text_part)

       
        server.sendmail(sender_email, email, msg.as_string())

    server.quit()

emails = ['recipient1@example.com', 'recipient2@example.com']
text = 'Hello, this is a test email.'
send_emails(emails, text)