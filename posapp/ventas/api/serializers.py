from rest_framework import serializers
from ventas.models import Venta

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'