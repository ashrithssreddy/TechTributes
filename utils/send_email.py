import smtplib
import yaml
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Load configuration from config.yaml
with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Gmail credentials
email_sender = config['gmail']['email_sender']
email_password = config['gmail']['email_password']
email_receiver = config['gmail']['email_receiver']

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [24, 30, 22]}
df = pd.DataFrame(data)

# Create the email content
subject = "Test Email with DataFrame and Image"
html_body = f"""
<html>
<head></head>
<body>
    <h2>This is a test email</h2>
    
    {df.to_html(index=False)}
    
    <img src="cid:image1" alt="Embedded Image"/>
</body>
</html>
"""

# Create the email message
msg = MIMEMultipart('related')
msg['From'] = email_sender
msg['To'] = email_receiver
msg['Subject'] = subject

# Attach the HTML content
msg_html = MIMEText(html_body, 'html')
msg.attach(msg_html)

# Attach the image, optionally
with open('img/logo.jpg', 'rb') as img_file:
    img = MIMEImage(img_file.read())
    img.add_header('Content-ID', '<image1>')
    msg.attach(img)

# Send the email using Gmail's SMTP server
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Secure the connection
        server.login(email_sender, email_password)
        server.send_message(msg)
        print(f"Email sent successfully to {email_receiver}")
except Exception as e:
    print(f"Failed to send email: {e}")
