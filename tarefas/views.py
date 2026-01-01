from django.shortcuts import render, redirect
from .models import Tarefa

def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/listar.html', {'tarefas': tarefas})

def nova_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        
        Tarefa.objects.create(titulo=titulo, descricao=descricao)

        return redirect('listar_tarefas')
    
    return render(request, 'tarefas/nota.html')