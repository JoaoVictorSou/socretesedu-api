from django.contrib import admin
from .models import Aluno, Matricula
# Register your models here.

class Alunos(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'rg',
        'cpf',
        'nascimento',
    )
    list_display_links = (
        'id',
        'nome',
    )
    search_fields = ( 'nome', )
    list_per_page = 20

admin.site.register(Aluno, Alunos)

class Matriculas(admin.ModelAdmin):
    list_display = (
        'id',
        'aluno',
        'curso',
        'periodo',
    )
    list_display_links = (
        'id',
        'aluno',
    )

admin.site.register(Matricula, Matriculas)