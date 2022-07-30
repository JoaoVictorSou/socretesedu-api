# Este arquivo será uma ponte enttre o JSON e o código Python na API
from rest_framework import serializers
from .models import Aluno

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