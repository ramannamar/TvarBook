from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, generics
from rest_framework.response import Response
from .models import UserNet
from .serializers import GetUserNetSerializer, GetUserNetPublicSerializer, RegisterUserSerializer
from rest_framework import generics
from django.contrib.auth.hashers import make_password
from .serializers import RegisterUserSerializer


class UserNetPublicView(ModelViewSet):
    """ Displaying a user's public profile
    """
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetPublicSerializer
    permission_classes = [permissions.AllowAny]


class UserNetView(ModelViewSet):
    """ User profile display
    """
    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)


class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    """Serializer for password hashing
    """
    def perform_create(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)

    """ for registration
    """
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({'message': 'Registration successful'}, status=201)
        else:
            return Response(serializer.errors, status=400)




