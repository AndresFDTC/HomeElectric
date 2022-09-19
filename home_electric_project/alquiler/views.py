from .serializers import ToolSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Herramienta

# Create your views here.
class RegisterTool(generics.CreateAPIView):
    queryset = Herramienta.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ToolSerializer
    
class ListTool(generics.ListAPIView):
    queryset = Herramienta.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ToolSerializer