from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .serializers import *


class AboutMeViewSet(ModelViewSet):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer
    permission_classes = [AllowAny]


class ContactsViewSet(ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = AboutMeSerializer
    permission_classes = [AllowAny]

