# Em colaboradores/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Read (Listar)
    path('', views.colaborador_lista, name='index'), 
    
    # Create (Cadastrar)
    path('cadastro/', views.colaborador_novo, name='cadastro'),
    

    # <int:id> pega o número do colaborador da URL
    path('editar/<int:id>/', views.colaborador_editar, name='colaborador_editar'),
    
    # Delete (Excluir) - NOVA LINHA
    path('excluir/<int:id>/', views.colaborador_excluir, name='colaborador_excluir'),
]