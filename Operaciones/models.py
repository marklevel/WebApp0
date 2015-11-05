from django.db import models

from Oficinas.models import Sucursale, Departamento
from Maquinas.models import Cofre

class Deposito(models.Model):
	id_sucursal = models.ForeignKey(Sucursale)
	id_departamento = models.ForeignKey(Departamento)
	id_cofre = models.ForeignKey(Cofre)
	id_transaccion = models.PositiveIntegerField()
	cajero = models.PositiveIntegerField()
	unidades = models.PositiveIntegerField()
	denominacion = models.PositiveIntegerField()
	fecha_depo = models.DateTimeField(null=True, blank=True)

class Colecta(models.Model):
	id_sucursal = models.ForeignKey(Sucursale)
	id_departamento = models.ForeignKey(Departamento)
	id_cofre = models.ForeignKey(Cofre)
	id_transaccion = models.PositiveIntegerField()
	cajero = models.PositiveIntegerField()
	unidades = models.PositiveIntegerField()
	denominacion = models.PositiveIntegerField()
	fecha_colec = models.DateTimeField(null=True, blank=True)

class Evento(models.Model):
	id_sucursal = models.ForeignKey(Sucursale)
	id_departamento = models.ForeignKey(Departamento)
	id_cofre = models.ForeignKey(Cofre)
	id_mensaje = models.PositiveIntegerField()
	cajero = models.PositiveIntegerField()
	fecha_event = models.DateTimeField(null=True, blank=True)

class Estatu(models.Model):
	id_sucursal = models.ForeignKey(Sucursale)
	id_departamento = models.ForeignKey(Departamento)
	id_cofre = models.ForeignKey(Cofre)
	id_mensaje = models.PositiveIntegerField()
	cajero = models.PositiveIntegerField()
	fecha_esta = models.DateTimeField(null=True, blank=True)
