import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# Enter your mail address here.
email_config = ""

# Enter your password application here.
password_config = ""

# Connect to the SMTP server using the Gmail SMTP server and port 25.
# This connection will be used to send emails.
smtp_server = smtplib.SMTP("smtp.gmail.com", 587)



# Send the EHLO command to the SMTP server to start the conversation.
# This is required before sending any email.
smtp_server.ehlo()

smtp_server.starttls()
smtp_server.ehlo()

# Log in to the SMTP server using the email address and password.

smtp_server.login(email_config, password_config)

msg = MIMEMultipart()
msg["From"] = email_config
msg["To"] = email_config
msg["Subject"] = "Don't wory it's just a test!"

with open("message.txt", "r") as f:
    message = f.read()

msg.attach(MIMEText(message, "plain"))

file_name = "code.jpg"
attachment = open(f"{file_name}",  "rb") 

p = MIMEBase('application', 'octet-stream')

p.set_payload(attachment.read())

encoders.encode_base64(p)

p.add_header('content-Disposition', f'attachement; filename={file_name}')

msg.attach(p)

text = msg.as_string()

# Enter the sender email address and the recipient email address.
smtp_server.sendmail('', '', text)
