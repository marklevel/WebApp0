from django.contrib import admin

from .models import Pai, Estado, Ciudade, Moneda

class modeloPais(admin.ModelAdmin):
	list_display = ('idCountry', 'country_name')

class modeloEstado(admin.ModelAdmin):
	list_display = ('idState', 'state_name', 'pais')

class modeloCiudad(admin.ModelAdmin):
	list_display = ('idCity', 'city_name', 'estado')

admin.site.register(Pai, modeloPais)
admin.site.register(Estado, modeloEstado)
admin.site.register(Ciudade, modeloCiudad) 
admin.site.register(Moneda)
