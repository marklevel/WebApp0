from django.contrib import admin

from .models import Deposito, Colecta, Evento, Estatu

admin.site.register(Deposito)
admin.site.register(Colecta)
admin.site.register(Evento)
admin.site.register(Estatu)