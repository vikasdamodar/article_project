from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage

EMAIL_MIR_ADDRESS = "debug@mir.de"
EMAIL_SEND_FROM = "test@test.com"


class ContactRequest(models.Model):
    """ Contact Request data """
    email = models.EmailField()
    name = models.CharField(max_length=50)
    content = models.TextField()
    request_date = models.DateField(auto_now_add=True)


@receiver(post_save, sender=ContactRequest)
def send_contact_request_email(sender, instance, **kwargs):
    """ Email Contact request details to authority"""
    email_body = f"Name: {instance.name}, Email: {instance.email}, Content: {instance.content}"
    # Not configured for live email sending
    send_email = EmailMessage(
        f"New Contact Request from - {instance.name}",
        email_body,
        EMAIL_SEND_FROM,
        [EMAIL_MIR_ADDRESS],
        reply_to=[instance.email]
    )
    send_email.send()
