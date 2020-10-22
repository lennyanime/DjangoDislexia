from rest_framework import serializers
from apps.dyslexia.models import Especialista
from apps.dyslexia.models import Niño
from apps.dyslexia.models import Diagnostico

class EspecialistaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Especialista
        fields=['id_especialista','nombre','profesion']

class NiñoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Niño
        fields=['id_niño','nombre','edad','especialista']

class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Diagnostico
        fields=['id_diagnostico','resultado','descripcion','especialista']