from django.contrib import admin
from .models import Curso
# Register your models here.

class Cursos(admin.ModelAdmin):
    list_display = (
        'id',
        'codigo_curso',
        'descricao',
        'nivel',
    )
    list_display_links = (
        'id',
        'codigo_curso',
        'descricao',
    )
    search_fields = (
        'codigo_curso',
        'descricao',
    )

admin.site.register(Curso, Cursos)
