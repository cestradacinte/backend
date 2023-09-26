from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ventas.api.views import VentaApiViewSet

router_ventas = DefaultRouter()
router_ventas.register(prefix='ventas', basename='ventas', viewset=VentaApiViewSet)

urlpatterns = [
    path('', include(router_ventas.urls)),
]