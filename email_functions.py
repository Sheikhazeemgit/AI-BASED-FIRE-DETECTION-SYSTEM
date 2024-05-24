import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_mail_function(sender_email, app_password, recipient_email, message_text, attachment_path):
    try:
        # Create a multipart message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = "Fire Detection Alert"

        # Add message body
        message.attach(MIMEText(message_text, "plain"))

        # Add attachment
        if attachment_path:
            filename = os.path.basename(attachment_path)
            with open(attachment_path, "rb") as attachment_file:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment_file.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename= {filename}")
            message.attach(part)

        # Connect to the SMTP server and send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(sender_email, app_password)
            server.send_message(message)
        print("Alert email sent successfully to {}".format(recipient_email))
    except smtplib.SMTPException as e:
        print("Error sending email:", str(e))
