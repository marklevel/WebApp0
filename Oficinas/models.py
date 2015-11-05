from django.db import models

class Sucursale(models.Model):
	id_sucursal = models.PositiveIntegerField()
	Nombre = models.CharField(max_length=300)
	ubicacion = models.CharField(max_length=300)
	descripcion = models.CharField(max_length=300)

	def __str__(self):
		return u'%s' % (self.Nombre)

class Departamento(models.Model):
	id_departamento = models.PositiveIntegerField()
	Nombre = models.CharField(max_length=300)
	descripcion = models.TextField(max_length=500)

	def __str__(self):
		return u'%s' % (self.Nombre)