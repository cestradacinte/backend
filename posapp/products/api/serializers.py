from rest_framework import serializers
from products.models import Nevado, Taco

class NevadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nevado
        fields = ['nombre', 'tipo', 'vaso', 'pitillo', 'precio']
        
class TacoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taco
        fields = ['nombre', 'carne', 'pesocarne', 'precio']