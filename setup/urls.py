"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Importa as funcionalidades de administração do Django.
from django.contrib import admin
# Importa as funções 'path' (para definir rotas) e 'include' (para incluir URLs de outros apps).
from django.urls import path, include


# O 'urlpatterns' é a lista padrão que o Django procura para definir as rotas do site.
urlpatterns = [
    # Define a rota para o painel de administração do Django.
    # Qualquer URL que comece com 'admin/' será gerenciada pelo admin.site.urls.
    path('admin/', admin.site.urls),
    
    # Incluir URLs de aplicativos.
    # Define a rota raiz do site ('').
    # A função 'include()' diz ao Django para "passar" qualquer URL que chegue aqui 
    # (neste caso, qualquer URL que não seja 'admin/') para ser processada pelo 
    # arquivo 'urls.py' dentro do aplicativo 'colaboradores'.
    # Isso mantém as URLs organizadas por aplicativo.
    path('', include('colaboradores.urls')), 
]