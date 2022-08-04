from rest_framework import viewsets
from .models import Aluno, Matricula
from .serializer import AlunoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaMatriculasCursoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class AlunosViewSet(viewsets.ModelViewSet):
    """
    Exibe todos os alunos(a) do SocretesEdu.
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MatriculasViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaMatriculasAlunos(viewsets.generics.ListAPIView):
    """
    Lista de matrículas referentes a um aluno
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaMatriculadosCurso(viewsets.generics.ListAPIView):
    """
    Lista todos os alunos de um curso.
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso = self.kwargs['curso_id'])

        return queryset
    
    serializer_class = ListaMatriculasCursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
