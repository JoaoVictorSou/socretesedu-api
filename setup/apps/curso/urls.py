from django.urls import path, include
from .views import CursosViewSet
from aluno.urls import router as rd
from rest_framework import routers

router = routers.SimpleRouter()
router.register('cursos', CursosViewSet, basename = "Cursos")

urlpatterns = [
    path('', include(router.urls)),
]