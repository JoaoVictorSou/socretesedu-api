from rest_framework import viewsets
from .models import Curso
from .serializer import CursoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CursosViewSet(viewsets.ModelViewSet):
    """
    Exibe todos os cursos ofertados no SocretesEdu
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]