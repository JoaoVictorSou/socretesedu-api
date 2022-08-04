# Este arquivo será uma ponte enttre o JSON e o código Python na API
from dataclasses import fields
from pyexpat import model
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

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source = 'curso.descricao')
    periodo = serializers.SerializerMethodField()
    
    class Meta:
        model = Matricula
        fields = [
            'curso',
            'periodo',
            ]
    
    def get_periodo(self, obj):
        """
        Método para pegar o período na forma por extenso, utilizado pelo SerializerMethodField
        """
        return obj.get_periodo_display()

class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    aluno = serializers.ReadOnlyField(source = 'aluno.nome')
    
    class Meta:
        model = Matricula
        fields = ['aluno']