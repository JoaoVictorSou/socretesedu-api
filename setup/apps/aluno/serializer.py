# Este arquivo será uma ponte enttre o JSON e o código Python na API
from dataclasses import fields
from rest_framework import serializers
from .models import Aluno, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = [
            'id',
            'nome',
            'rg',
            'cpf',
            'nascimento',
        ]

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = [
            'id',
            'aluno',
            'curso',
            'periodo',
        ]