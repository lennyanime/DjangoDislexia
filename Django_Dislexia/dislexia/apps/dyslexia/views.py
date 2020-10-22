#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from apps.dyslexia.models import Especialista
from apps.dyslexia.models import Niño
from apps.dyslexia.models import Diagnostico
from apps.dyslexia.serializer import EspecialistaSerializer
from apps.dyslexia.serializer import NiñoSerializer
from apps.dyslexia.serializer import DiagnosticoSerializer
from rest_framework.decorators import api_view
from rest_framework import status



@api_view(['GET'])
def GetEspecialistas(request):
    if request.method=='GET':
        Especialistas=Especialista.objects.all()
        serializer=EspecialistaSerializer(Especialistas, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET','PUT','DELETE'])
def Especialistas(request,key):
    try:
        esp=Especialista.objects.get(pk=key)
    except Especialista.DoesNotExist:
        return HttpResponse(status=status.HTPP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=EspecialistaSerializer(esp)#para convertir datos del modelo en un formato json
        return JsonResponse(serializer.data)
    elif request.method=='PUT':
        data=JSONParser().parse(request)
        serializer=EspecialistaSerializer(esp,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        esp.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def SaveEspecialistas(request):
    save_e=EspecialistaSerializer(data=request.data)
    if save_e.is_valid():
        save_e.save()
        return JsonResponse(save_e.data)

#sección niños

@api_view(['GET'])
def GetNiños(request):
    if request.method=='GET':
        Niños=Niño.objects.all()
        serializer=NiñoSerializer(Niños, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET','PUT','DELETE'])
def Niños(request,key):
    try:
        n=Niño.objects.get(pk=key)
    except Niño.DoesNotExist:
        return HttpResponse(status=status.HTPP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=NiñoSerializer(n)#para convertir datos del modelo en un formato json
        return JsonResponse(serializer.data)
    elif request.method=='PUT':
        data=JSONParser().parse(request)
        serializer=NiñoSerializer(n, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        n.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def SaveNiños(request):
    save_n=NiñoSerializer(data=request.data)
    if save_n.is_valid():
        save_n.save()
        return JsonResponse(save_n.data)

#sección diagnóstico

@api_view(['GET'])
def GetDiagnosticos(request):
    if request.method=='GET':
        Diagnosticos=Diagnostico.objects.all()
        serializer=DiagnosticoSerializer(Diagnosticos, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET','PUT','DELETE'])
def Diagnosticos(request,key):
    try:
        d=Diagnostico.objects.get(pk=key)
    except Diagnostico.DoesNotExist:
        return HttpResponse(status=status.HTPP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=DiagnosticoSerializer(d)#para convertir datos del modelo en un formato json
        return JsonResponse(serializer.data)
    elif request.method=='PUT':
        data=JSONParser().parse(request)
        serializer=DiagnosticoSerializer(d, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        d.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def SaveDiagnosticos(request):
    save_d=DiagnosticoSerializer(data=request.data)
    if save_d.is_valid():
        save_d.save()
        return JsonResponse(save_d.data)


