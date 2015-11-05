from django.shortcuts import render
from rest_framework import viewsets
from Configuraciones.serializers import PaisSerializer

from django.views.generic.detail import DetailView
from django.views.generic import ListView

from .models import Pai

class PaisViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Pai.objects.all()
    serializer_class = PaisSerializer