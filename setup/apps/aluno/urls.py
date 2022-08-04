from django import views
from django.urls import path, include
from .views import AlunosViewSet, MatriculasViewSet, ListaMatriculasAlunos, ListaMatriculadosCurso
from rest_framework import routers

router = routers.SimpleRouter()
router.register('alunos', AlunosViewSet, basename = "Alunos")
router.register('matriculas', MatriculasViewSet, 'Matriculas')

urlpatterns = [
    path('', include(router.urls)),
    path('alunos/<int:pk>/matriculas/', ListaMatriculasAlunos.as_view(), name = 'lista_matriculas_alunos'),
    path('cursos/<int:curso_id>/matriculas/', ListaMatriculadosCurso.as_view(), name = 'lista_matriculas_cursos'),
]