from django.test import TestCase
from django.urls import reverse
from django.core import mail

from contact.models import ContactRequest, EMAIL_SEND_FROM, EMAIL_MIR_ADDRESS


class ContactRequestTC(TestCase):
    def setUp(self) -> None:
        """ Setup test data """

    def test_create_contact_request(self):
        """ Test contact request creates an entry in DB"""
        request_data = {"email": "Testemail@test.com", "name": "TestUser", "content": "Test C"}
        self.client.post(reverse("contact_request"), data=request_data)
        created_obj = ContactRequest.objects.latest('request_date')
        self.assertEqual(request_data['email'], created_obj.email)
        self.assertEqual(request_data['name'], created_obj.name)
        self.assertEqual(request_data['content'], created_obj.content)

    def test_contact_request_email(self):
        request_data = {"email": "Testemail@test.com", "name": "TestUser", "content": "Test C"}
        self.client.post(reverse("contact_request"), data=request_data)
        email_sent = mail.outbox[0]

        self.assertEqual(email_sent.to, [EMAIL_MIR_ADDRESS])
        self.assertEqual(email_sent.from_email, EMAIL_SEND_FROM)
        # Check reply to added properly
        self.assertEqual([request_data['email']], email_sent.reply_to)
        # Check email body
        email_body = f"Name: {request_data['name']}," \
                                  f" Email: {request_data['email']}," \
                                  f" Content: {request_data['content']}"
        self.assertEqual(email_sent.body, email_body)

