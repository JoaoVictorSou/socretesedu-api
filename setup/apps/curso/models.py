from django.db import models

# Create your models here.

class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    
    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices = NIVEL, blank = False, null = False, default = 'B') # Este campo possue opçõesreturn 

    def __str__(self):
        return self.descricao
