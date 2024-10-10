# tarefas/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TarefaViewSet, UserViewSet

router = DefaultRouter()
router.register(r'tarefas', TarefaViewSet)
router.register(r'usuarios', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
