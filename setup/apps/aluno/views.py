from rest_framework import viewsets
from .models import Aluno, Matricula
from .serializer import AlunoSerializer, MatriculaSerializer

# Create your views here.

class AlunosViewSet(viewsets.ModelViewSet):
    """
    Exibe todos os alunos(a) do SocretesEdu.
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class MatriculasViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer