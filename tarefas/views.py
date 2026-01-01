from django.shortcuts import render
from .models import Tarefa

# Create your views here.
def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/listar.html', {'tarefas': tarefas})