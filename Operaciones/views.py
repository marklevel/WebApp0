# from django.shortcuts import render
from rest_framework import viewsets

from Operaciones.serializers import DepositosSerializer, ColectasSerializer, EventosSerializer, EstatusSerializer
from .models import Deposito, Colecta, Evento, Estatu

class DepositosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Deposito.objects.all()
    serializer_class = DepositosSerializer

class ColectasViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Colecta.objects.all()
    serializer_class = ColectasSerializer

class EventosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Evento.objects.all()
    serializer_class = EventosSerializer

class EstatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Estatu.objects.all()
    serializer_class = EstatusSerializer
