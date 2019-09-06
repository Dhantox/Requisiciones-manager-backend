from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status, permissions
from requisiciones.models import Requisicion
from requisiciones.serializers import RequisicionSerializer

class RequisicionesViewSet(ViewSet):

    def list(self, request):
        queryset = Requisicion.objects.all()
        serializer = RequisicionSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        serializer = RequisicionSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)