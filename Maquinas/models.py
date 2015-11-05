from django.db import models

from Configuraciones.models import Pai, Estado, Ciudade

class Equipo(models.Model):
	id_machine = models.PositiveIntegerField()
	marca = models.CharField(max_length=300)
	modelo = models.CharField(max_length=300)
	descripcion = models.CharField(max_length=500)

	def __str__(self):
		return self.modelo

class Cofre(models.Model):
	id_cofre = models.PositiveIntegerField()
	id_machine = models.ForeignKey(Equipo)
	no_serie= models.CharField(max_length=100)
	nombre = models.CharField(max_length=150)
	direccion = models.CharField(max_length=300)
	pais = models.ForeignKey(Pai)
	estado = models.ForeignKey(Estado)
	ciudad = models.ForeignKey(Ciudade)
	ubicacion = models.CharField(max_length=300)
	descripcion = models.CharField(max_length=500)

	def __str__(self):
		return self.nombre