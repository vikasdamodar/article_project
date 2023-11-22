from rest_framework.serializers import ModelSerializer

from contact.models import ContactRequest


class ContactRequestSerializer(ModelSerializer):
    class Meta:
        """ Meta data"""
        model = ContactRequest
        fields = ['email', 'name', 'content']
