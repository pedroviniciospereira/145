from django.shortcuts import render, redirect
from .models import Colaborador
from django.db.models import Q 

# View para a página de LISTA (index.html)
def colaborador_lista(request):
    
    # Lógica de Pesquisa (lê o '?q=' da URL)
    query = request.GET.get('q', '')
    if query:
        colaboradores = Colaborador.objects.filter(
            Q(nome_completo__icontains=query) |
            Q(cpf__icontains=query) |
            Q(funcao__icontains=query)
        ).order_by('-data_cadastro')
    else:
        colaboradores = Colaborador.objects.all().order_by('-data_cadastro')
    
    # Lógica dos Cards (baseado no wireframe)
    total_colaboradores = colaboradores.count()
    colaboradores_ativos = colaboradores.filter(status='Ativo').count()
    colaboradores_inativos = total_colaboradores - colaboradores_ativos

    context = {
        'colaboradores_lista': colaboradores,
        'total_colaboradores': total_colaboradores,
        'colaboradores_ativos': colaboradores_ativos,
        'colaboradores_inativos': colaboradores_inativos,
        'search_query': query # Para manter o texto na barra de pesquisa
    }
    return render(request, 'index.html', context)


# A função colaborador_novo (do cadastro) continua exatamente igual
def colaborador_novo(request):
    if request.method == 'POST':
        nome = request.POST.get('nome_completo')
        cpf = request.POST.get('cpf')
        funcao = request.POST.get('funcao')
        status = request.POST.get('status')
        
        cpf_limpo = ''.join(filter(str.isdigit, cpf))
        
        Colaborador.objects.create(
            nome_completo=nome,
            cpf=cpf_limpo,
            funcao=funcao,
            status=status
        )
        
        return redirect('index')

    return render(request, 'cadastro.html')