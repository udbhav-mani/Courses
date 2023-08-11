import smtplib
from email.message import EmailMessage

email_contents = """
This is a python generated mail."""

email = EmailMessage()
email["subject"] = ""
email["From"] = ""
email["To"] = ""

email.set_content(email_contents)

smtp_connector = smtplib.SMTP(host="smt.gmail.com", port=587)
smtp_connector.starttls()
smtp_connector.login("hg@hj.vnj", "fdvxzc")

smtp_connector.send_message(email)
smtp_connector.quit()
