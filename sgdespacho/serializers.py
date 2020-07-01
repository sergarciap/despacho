from rest_framework import serializers
from .models import Paquete,Bodega,Boleta

class PaqueteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paquete
        fields= '__all__'

class BodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Bodega
        fields='__all__'

class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Boleta
        fields='__all__'




