from django.db import models

class Pai(models.Model):
	idCountry = models.PositiveIntegerField()
	country_name = models.CharField(max_length=200)

	def __str__(self):
		return u'%s' % (self.country_name)

class Estado(models.Model):
	idState = models.PositiveIntegerField()
	state_name = models.CharField(max_length=100)
	pais = models.ForeignKey(Pai)

	def __str__(self):
		return u'%s' % (self.state_name)

class Ciudade(models.Model):
	idCity = models.PositiveIntegerField()
	city_name = models.CharField(max_length=200)
	estado = models.ForeignKey(Estado)

	def __str__(self):
		return u'%s' % (self.city_name)

class Moneda(models.Model):
	id_currency = models.PositiveIntegerField()
	Moneda = models.CharField(max_length=100)
	CurrencyCode = models.CharField(max_length=10)
	Denominacion = models.PositiveIntegerField()

	def __str__(self):
		return u'%s' % (self.Moneda)