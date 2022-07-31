from pyexpat import model
from tkinter import CASCADE
from django.db import models
from curso.models import Curso

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Matricula(models.Model):
    PERIODO = (
        ('M', 'matutino'),
        ('V', 'vespertino'),
        ('N', 'noturno'),
    )

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')

    def __str__(self):
        return f"Matrícula: {self.aluno} | {self.curso}"