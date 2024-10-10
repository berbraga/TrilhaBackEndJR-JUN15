# tarefas/serializers.py
from rest_framework import serializers
from .models import Tarefa, User

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'  # Inclui todos os campos do modelo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'date_joined']  # Campos do modelo User
