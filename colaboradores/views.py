# 1. Adicione get_object_or_404 aqui
from django.shortcuts import render, redirect, get_object_or_404 
from .models import Colaborador
from django.db.models import Q

# View de LISTA (index.html) 
def colaborador_lista(request):
    query = request.GET.get('q', '')
    if query:
        colaboradores = Colaborador.objects.filter(
            Q(nome_completo__icontains=query) |
            Q(cpf__icontains=query) |
            Q(funcao__icontains=query)
        ).order_by('-data_cadastro')
    else:
        colaboradores = Colaborador.objects.all().order_by('-data_cadastro')
    
    total_colaboradores = colaboradores.count()
    colaboradores_ativos = colaboradores.filter(status='Ativo').count()
    colaboradores_inativos = total_colaboradores - colaboradores_ativos

    context = {
        'colaboradores_lista': colaboradores,
        'total_colaboradores': total_colaboradores,
        'colaboradores_ativos': colaboradores_ativos,
        'colaboradores_inativos': colaboradores_inativos,
        'search_query': query
    }
    return render(request, 'index.html', context)


# View de CADASTRO (cadastro.html) 
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


# === 2. ADICIONE ESTA NOVA FUNÇÃO (UPDATE) ===
def colaborador_editar(request, id):
    # Busca o colaborador ou dá erro 404 se não achar
    colaborador = get_object_or_404(Colaborador, id=id)

    if request.method == 'POST':
        # Pega os dados do formulário enviado
        colaborador.nome_completo = request.POST.get('nome_completo')
        colaborador.cpf = ''.join(filter(str.isdigit, request.POST.get('cpf'))) # Limpa CPF
        colaborador.funcao = request.POST.get('funcao')
        colaborador.status = request.POST.get('status')
        
        # Salva as alterações no banco
        colaborador.save()
        
        # Redireciona para a lista
        return redirect('index')

    # Se for GET (só abriu a página de editar), envia o colaborador para o template
    context = {
        'colaborador': colaborador # A chave 'colaborador' é usada no HTML
    }
    # Reutiliza o mesmo template do cadastro
    return render(request, 'cadastro.html', context)


# === 3. ADICIONE ESTA NOVA FUNÇÃO (DELETE) ===
def colaborador_excluir(request, id):
    # Busca o colaborador ou dá erro 404
    colaborador = get_object_or_404(Colaborador, id=id)
    
    # Deleta o colaborador do banco
    colaborador.delete()
    
    # Redireciona para a lista
    return redirect('index')