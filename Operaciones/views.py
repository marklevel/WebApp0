from django.shortcuts import render
from rest_framework import viewsets
from Operaciones.serializers import DepositoSerializer
from Oficinas.models import Sucursale, Departamento

from django.views.generic.detail import DetailView
from django.views.generic import ListView

from .models import Deposito

class DepositoDetailView(DetailView):
	model = Deposito 

	def get_template_names(self):
		return 'depositos.html'

class DepositoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Deposito.objects.all()
    serializer_class = DepositoSerializer
