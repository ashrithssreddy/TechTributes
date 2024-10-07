import smtplib
import yaml
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64

# Load configuration from config.yaml
with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Gmail credentials
email_sender = config['gmail']['email_sender']
email_password = config['gmail']['email_password']
email_receiver = config['gmail']['email_receiver']

# Create the email content
## Include df optionally
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [24, 30, 22]}
df = pd.DataFrame(data)

## Include image optionally
with open('img/logo.jpg', 'rb') as img_file:
    image_data = img_file.read()
    image_base64 = base64.b64encode(image_data).decode('utf-8')

subject = "Test Email"
body = f"""
<html>
<head></head>
<body>
    <h2>This is a test email</h2>
    {df.to_html(index=False)}
    <img src="data:image/jpeg;base64,{image_base64}" alt="Embedded Image"/>
</body>
</html>
"""

# Create the email message
msg = MIMEMultipart('alternative')
msg['From'] = email_sender
msg['To'] = email_receiver
msg['Subject'] = subject
msg.attach(MIMEText(body, 'html')) # 'plain'

# Send the email using Gmail's SMTP server
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Secure the connection
        server.login(email_sender, email_password)
        server.send_message(msg)
        print(f"Email sent successfully to {email_receiver}")
except Exception as e:
    print(f"Failed to send email: {e}")
