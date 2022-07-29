from django.http import JsonResponse

# Create your views here.

def alunos(request):
    return JsonResponse({'teste': 1})