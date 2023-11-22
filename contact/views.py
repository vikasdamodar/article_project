import json

from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from contact.models import ContactRequest
from contact.serializers import ContactRequestSerializer


class ContactRequestView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'contact_request.html'
    style = {'template_pack': 'rest_framework/vertical/'}

    def get(self, request):
        """ Render Form """
        serializer = ContactRequestSerializer()
        return Response({'serializer': serializer, 'style': self.style})

    def post(self, request):
        """ Create Contact request"""
        serializer = ContactRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('contact_request')
        return HttpResponse(json.dumps(serializer.errors))
