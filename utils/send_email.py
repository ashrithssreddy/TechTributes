import smtplib
import yaml
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load configuration from config.yaml
with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Gmail credentials
email_sender = config['gmail']['email_sender']
email_password = config['gmail']['email_password']
email_receiver = config['gmail']['email_receiver']

# Create the email content
subject = "Test Email"
body = "This is a test email sent using Python and the configuration file."

# Create the email message
msg = MIMEMultipart()
msg['From'] = email_sender
msg['To'] = email_receiver
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Send the email using Gmail's SMTP server
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Secure the connection
        server.login(email_sender, email_password)
        server.send_message(msg)
        print(f"Email sent successfully to {email_receiver}")
except Exception as e:
    print(f"Failed to send email: {e}")
