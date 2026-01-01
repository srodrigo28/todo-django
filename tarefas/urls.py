from django.urls import path
from . import views

urlpatterns = [
    path('',  views.listar_tarefas,   name='listar_tarefas'),
    
    path('nova/', views.nova_tarefa,  name='nova_tarefa'),

    path('editar/<int:tarefa_id>',  views.editar_tarefa,   name='editar_tarefa'),
    
    path('tarefa/<int:tarefa_id>/', views.detalhe_tarefa,  name='detalhe_tarefa'),
    
    path('deletar/<int:tarefa_id>', views.deletar_tarefa,  name='deletar_tarefa'),
]

# Constuindo um fluxo básico para crud
# visto que já tenho um fluxo para tarefa
# quero criar uma pagina inicial nela o usuário pode se cadastrar
# criando um novo usuário

# criando migration
# novo_user: nome, email, telefone e senha