from django.shortcuts import render, redirect, get_object_or_404
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
    
    return render(request, 'tarefas/nova.html')

def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)

    if request.method == 'POST':
        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.finalizado = 'finalizado' in request.POST
        tarefa.save()
        return redirect('listar_tarefas')
    
    return render(request, 'tarefas/editar.html', {'tarefa': tarefa})