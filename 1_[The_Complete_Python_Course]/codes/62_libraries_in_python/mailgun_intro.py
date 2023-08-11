"""
we need to have a domain name"""
import requests

"""
we use requests"""


class Mailgun:
    MAILGUN_API_URL = ""
    MAILGUN_API_KEY = ""
    FROM_NAME = ""
    FROM_EMAIL = ""

    @classmethod
    def send_email(cls, to_mails, subject, content):
        requests.post(
            cls.MAILGUN_API_KEY,
            auth=("api", cls.MAILGUN_API_KEY),
            data={
                "from": f"{cls.FROM_EMAIL} <{cls.FROM_NAME}>",
                "to": to_mails,
                "subject": subject,
                "text": content,
            },
        )
