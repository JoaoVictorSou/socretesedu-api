from django import views
from django.urls import path, include
from .views import AlunosViewSet, MatriculasViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('alunos', AlunosViewSet, basename = "Alunos")
router.register('matriculas', MatriculasViewSet, 'Matriculas')

urlpatterns = [
    path('', include(router.urls)),
]