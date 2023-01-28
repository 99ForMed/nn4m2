
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class Email:
    author = ''
    subject = ''
    recipients = []
    body_html = None
    body_plain = ''
    attachments = []

    def __init__(self, email_package):
        self.author = email_package['author']
        self.subject = email_package['subject']
        self.recipients = email_package['recipients']
        self.body_html = render_to_string(email_package['template'], email_package['context'])
        self.body_plain = strip_tags(self.body_html)
        if 'files' in email_package.keys():
            self.attachments = email_package['files']
        
    def send(self):
        mail.send_mail(self.subject, self.body_plain, self.author, self.recipients, html_message = self.body_html, attachments = self.attachments)

def general_EMAIL(request, email_package, *args, **kwargs):
    try:
        email = Email(email_package)
        email.send()
            
    except ValueError as e:
        print(e)