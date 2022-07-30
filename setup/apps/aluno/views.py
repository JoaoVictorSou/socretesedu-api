from rest_framework import viewsets
from .models import Aluno
from .serializer import AlunoSerializer

# Create your views here.

class AlunosViewSet(viewsets.ModelViewSet):
    """
    Exibe todos os alunos(a) do SocretesEdu.
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer