from django.shortcuts import render
from rest_framework import viewsets
from .models import Consult
from .serializer import ConsultSerializer
from django.core.mail import EmailMessage
from rest_framework import generics



class ConsultViewSet(generics.ListCreateAPIView):
    queryset = Consult.objects.all()
    serializer_class = ConsultSerializer

    def send_email(request):
        email = EmailMessage(
            'Title',
            (ConsultSerializer.name, ConsultSerializer.email, ConsultSerializer.phone),
            'ds8736317@gmail.com',
            ['diptiranjansahu999@gmail.com']
        )
        # email.attach_file(ConsultSerializer.file)
        email.send()

        

        
