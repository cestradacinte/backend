from rest_framework import viewsets
from products.models import Nevado, Taco
from products.api.serializers import NevadoSerializer, TacoSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class NevadoApiViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Nevado.objects.all()
    serializer_class = NevadoSerializer
    
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        return super().create(request, *args, **kwargs)
    
class TacoApiViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Taco.objects.all()
    serializer_class = TacoSerializer
    
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        return super().create(request, *args, **kwargs)