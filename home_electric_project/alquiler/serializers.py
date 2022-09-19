from alquiler.models import Herramienta
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Herramienta


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Herramienta
        fields = '__all__'
        