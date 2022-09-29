from django.shortcuts import render
from .serializers import RegisterSerializer, UserSerializer, InfoUserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics, status
from django.contrib.auth.models import User

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
class RegisterList(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class RetrieveUser(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    lookup_field = 'username'

class InfoUser(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = InfoUserSerializer
    lookup_field = 'pk'
    
class UpdateUser(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = InfoUserSerializer
    lookup_field = 'pk'