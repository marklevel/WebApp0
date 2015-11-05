from .models import Deposito
from rest_framework import serializers
from Oficinas.models import Sucursale, Departamento


class DepositoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deposito
        fields = ('id_sucursal', 'id_departamento', 'id_cofre', 'id_transaccion', 'cajero', 'unidades', 'denominacion', 'fecha_depo')
