from .models import Pai
from rest_framework import serializers


class PaisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pai
        fields = ('idCountry', 'country_name')
