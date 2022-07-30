from django import views
from django.urls import path, include
from .views import AlunosViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('alunos', AlunosViewSet, basename = "Alunos")

urlpatterns = [
    path('', include(router.urls)),
]