from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from user.api.views import UserView, UserApiViewSet

router_user = DefaultRouter()
router_user.register(prefix='user', basename='users', viewset=UserApiViewSet)

urlpatterns = [
    path('auth/login', TokenObtainPairView.as_view(), name='login'),
    path('auth/me',  UserView.as_view(), name='me')
]