from rest_framework import serializers

from .models import Deposito, Colecta, Evento, Estatu

class DepositosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deposito
        fields = ('id_sucursal', 'id_departamento', 'id_cofre', 'id_transaccion', 'cajero', 'unidades', 'denominacion', 'fecha_depo')

class ColectasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Colecta
        fields = ('id_sucursal', 'id_departamento', 'id_cofre', 'id_transaccion', 'cajero', 'unidades', 'denominacion', 'fecha_colec')

class EventosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = ('id_sucursal', 'id_departamento', 'id_cofre', 'id_mensaje', 'cajero', 'fecha_event')

class EstatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estatu
        fields = ('id_sucursal', 'id_departamento', 'id_cofre', 'id_mensaje', 'cajero', 'fecha_esta')