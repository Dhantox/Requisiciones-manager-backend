from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth.models import User
from usuarios.serializers import UsuarioSerializer

class UsuariosViewSet(ViewSet):

    def list(self, request):
        queryset = User.objects.all()
        serializer = UsuarioSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def create(self, request):
        print(request.data)
        usuario = User()
        usuario.username = request.data["usuario"]
        usuario.email = request.data["correo"]
        usuario.first_name = request.data["nombre"]
        usuario.last_name = request.data["apellido"]
        usuario.save()
        return Response(status=status.HTTP_200_OK)

