from django.shortcuts import render

from projects.serializers import ProjectSerializer
from .models import Project
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status

class AdquisicionViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer

    @action(detail=True, methods=['post'])
    def modificar(self,request,pk=None):
        task = self.get_object()
        task.done = not task.done
        task.save()
        return Response({
            'status':'task done' if task.done else 'task undone'
        }, status=status.HTTP_200_OK)