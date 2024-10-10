from django.shortcuts import render

# tarefas/views.py
from rest_framework import viewsets
from .models import Tarefa, User
from .serializers import TarefaSerializer, UserSerializer

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
