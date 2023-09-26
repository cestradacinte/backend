from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.api.views import NevadoApiViewSet, TacoApiViewSet

router_product = DefaultRouter()
router_product.register(prefix='nevado', basename='nevado', viewset=NevadoApiViewSet)
router_product.register(prefix='taco', basename='taco', viewset=TacoApiViewSet)

urlpatterns = [
    path('', include(router_product.urls)),
]