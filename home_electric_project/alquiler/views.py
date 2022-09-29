from .serializers import ToolSerializer, RentSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Herramienta, Alquiler

# CRUD herramientas
# Create Herramienta:
class RegisterTool(generics.CreateAPIView):
    queryset = Herramienta.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ToolSerializer

# Lista de Herramientas:
class ListTool(generics.ListAPIView):
    queryset = Herramienta.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ToolSerializer

# Read Herramienta:
class RetrieveTool(generics.RetrieveAPIView):
    queryset = Herramienta.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ToolSerializer
    lookup_field = 'pk'

# Update Herramienta:
class UpdateTool(generics.UpdateAPIView):
    queryset = Herramienta.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ToolSerializer
    lookup_field = 'pk'

# Delete Herramienta:
class DeleteTool(generics.DestroyAPIView):
    queryset = Herramienta.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ToolSerializer
    lookup_field = 'pk'

# --------------------------------------------------
# CRUD de alquiler
# Create alquiler:
class RegisterRent(generics.CreateAPIView):
    queryset = Alquiler.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RentSerializer

# Lista de alquileres:
class ListRent(generics.ListAPIView):
    queryset = Alquiler.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RentSerializer
    '''lookup_field = 'pk'
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Alquiler.objects.filter(usuario=user)'''

# Read alquiler:
class RetrieveRent(generics.RetrieveAPIView):
    queryset = Alquiler.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RentSerializer
    lookup_field = 'pk'

# Update alquiler:
class UpdateRent(generics.UpdateAPIView):
    queryset = Alquiler.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RentSerializer
    lookup_field = 'pk'

# Delete alquiler:
class DeleteRent(generics.DestroyAPIView):
    queryset = Alquiler.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RentSerializer
    lookup_field = 'pk'
    
# Rents by user
class RentsByUser(generics.ListAPIView):
    def get_queryset(self):
        usuario_id = self.kwargs['usuario_id']
        return Alquiler.objects.filter(usuario_id=usuario_id)
    permission_classes = (AllowAny,)
    serializer_class = RentSerializer
    lookup_field = 'usuario_id'