from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.hashers import make_password

from user.models import User
from user.api.serializers import UserSerializer

class UserApiViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['password'] = make_password(data['password'])
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        user = self.get_object()
        if 'password' in request.data:
                request.data['password'] = make_password(request.data['password'])
                return super().update(request, *args, **kwargs)
        else:
            request.data.pop('password',None)
            return super().update(request, *args, **kwargs)

class UserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
