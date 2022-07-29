from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("alunos", views.alunos, name = "alunos"),
]