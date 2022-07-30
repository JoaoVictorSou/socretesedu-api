from rest_framework import viewsets
from .models import Curso
from .serializer import CursoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """
    Exibe todos os cursos ofertados no SocretesEdu
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer