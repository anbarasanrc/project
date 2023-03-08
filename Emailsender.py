import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Define the sender and recipient email addresses
sender_email = 'sender@example.com'
recipient_email = 'recipient@example.com'

# Create a message object
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = 'Test email'

# Add the message body
body = 'This is a test email'
message.attach(MIMEText(body, 'plain'))

# Add an attachment (optional)
filename = 'example.txt'
attachment = open(filename, 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment', filename=filename)
message.attach(part)

# Define the SMTP server and port
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Log in to the SMTP server and send the message
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(sender_email, 'password')
    text = message.as_string()
    server.sendmail(sender_email, recipient_email, text)
