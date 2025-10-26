from django.urls import path
from . import views

urlpatterns = [
    # URL para a página de lista/dashboard (Ex: http://127.0.0.1:8000/)
    # Ela chama a view 'colaborador_lista' e tem o nome 'index'
    path('', views.colaborador_lista, name='index'), 
    
    # URL para a página de cadastro (Ex: http://127.0.0.1:8000/cadastro/)
    # Ela chama a view 'colaborador_novo' e tem o nome 'cadastro'
    path('cadastro/', views.colaborador_novo, name='cadastro'),
]