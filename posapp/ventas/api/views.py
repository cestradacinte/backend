from rest_framework import viewsets
from ventas.models import Venta
from ventas.api.serializers import VentaSerializer
from rest_framework.permissions import IsAuthenticated

class VentaApiViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [IsAuthenticated]
    