# Importações necessárias do Django
# ================================
# 'render': Função para renderizar (desenhar) um template HTML com um contexto (dados).
# 'redirect': Função para redirecionar o navegador do usuário para outra URL.
# 'get_object_or_404': Função útil que tenta buscar um objeto no banco de dados; 
#                      se não encontrar, levanta automaticamente um erro HTTP 404 (Not Found).
from django.shortcuts import render, redirect, get_object_or_404 
# Importa o modelo 'Colaborador' definido no arquivo models.py deste mesmo app.
from .models import Colaborador
# Importa o objeto 'Q', que permite construir consultas complexas ao banco de dados 
# usando operadores lógicos como OR (|) e AND (&). Usado na pesquisa.
from django.db.models import Q

# View (Função) para a página de LISTA de Colaboradores (index.html)
# =================================================================
# Esta função é chamada quando uma requisição chega para a URL associada a ela (geralmente a raiz '/').
# O parâmetro 'request' contém informações sobre a requisição HTTP (método, dados GET/POST, etc.).
def colaborador_lista(request):
    
    # Lógica de Pesquisa
    # ------------------
    # Pega o valor do parâmetro 'q' da URL (ex: /?q=Ana). 
    # request.GET é um dicionário com os parâmetros GET. 
    # .get('q', '') busca a chave 'q'; se não existir, retorna uma string vazia ''.
    query = request.GET.get('q', '')
    
    # Se 'query' não estiver vazia (o usuário pesquisou algo)...
    if query:
        # Filtra os objetos Colaborador no banco de dados.
        # Colaborador.objects acessa o "manager" do modelo, que permite fazer consultas.
        # .filter() cria uma consulta WHERE no SQL.
        # Q(...) permite combinar condições:
        #   - nome_completo__icontains=query: Busca onde 'nome_completo' CONTÉM (ignorando maiúsc./min.) o texto da 'query'.
        #   - cpf__icontains=query: Busca onde 'cpf' CONTÉM o texto da 'query'.
        #   - funcao__icontains=query: Busca onde 'funcao' CONTÉM o texto da 'query'.
        #   - O operador | significa OR (OU).
        # .order_by('-data_cadastro'): Ordena os resultados pela data de cadastro, do mais novo para o mais antigo ('-' indica ordem decrescente).
        colaboradores = Colaborador.objects.filter(
            Q(nome_completo__icontains=query) |
            Q(cpf__icontains=query) |
            Q(funcao__icontains=query)
        ).order_by('-data_cadastro')
    # Senão (se 'query' estiver vazia, ou seja, sem pesquisa)...
    else:
        # Busca TODOS os objetos Colaborador no banco de dados.
        # .all() retorna um QuerySet com todos os registros.
        colaboradores = Colaborador.objects.all().order_by('-data_cadastro')
    
    # Lógica dos Cards de Estatística
    # -------------------------------
    # Conta o número total de colaboradores encontrados (seja na pesquisa ou todos).
    total_colaboradores = colaboradores.count()
    # Filtra os colaboradores encontrados para pegar apenas os com status 'Ativo' e conta quantos são.
    colaboradores_ativos = colaboradores.filter(status='Ativo').count()
    # Calcula os inativos subtraindo os ativos do total.
    colaboradores_inativos = total_colaboradores - colaboradores_ativos

    # Preparação do Contexto para o Template
    # -------------------------------------
    # 'context' é um dicionário Python. As chaves deste dicionário se tornarão
    # variáveis acessíveis dentro do template HTML (index.html).
    context = {
        # A chave 'colaboradores_lista' receberá o QuerySet (lista) de colaboradores.
        'colaboradores_lista': colaboradores,
        # As outras chaves receberão os valores calculados para os cards.
        'total_colaboradores': total_colaboradores,
        'colaboradores_ativos': colaboradores_ativos,
        'colaboradores_inativos': colaboradores_inativos,
        # Envia a 'query' de volta para preencher o campo de busca no HTML.
        'search_query': query 
    }
    # Renderização do Template
    # ------------------------
    # Chama a função 'render', passando:
    #   1. O objeto 'request'.
    #   2. O nome do arquivo de template a ser usado ('index.html').
    #   3. O dicionário 'context' com os dados a serem usados no template.
    # O Django processa o HTML, insere as variáveis do contexto e retorna a resposta HTTP completa.
    return render(request, 'index.html', context)


# View (Função) para a página de CADASTRO de Colaboradores (cadastro.html)
# ======================================================================
# Esta função é chamada para a URL '/cadastro/'.
def colaborador_novo(request):
    # Verifica se o método da requisição HTTP é POST. 
    # Isso acontece quando o usuário clica no botão "Salvar" do formulário.
    if request.method == 'POST':
        # Se for POST, extrai os dados enviados pelo formulário.
        # request.POST é um dicionário contendo os dados do formulário.
        # .get('nome_do_campo') busca o valor associado ao atributo 'name' do input HTML.
        nome = request.POST.get('nome_completo')
        cpf = request.POST.get('cpf') # Vem com a máscara (ex: 123.456.789-01)
        funcao = request.POST.get('funcao')
        status = request.POST.get('status')
        
        # Limpa o CPF: Remove a máscara (pontos e traço) antes de salvar no banco.
        # filter(str.isdigit, cpf) pega apenas os caracteres que são dígitos.
        # ''.join(...) junta esses dígitos de volta em uma string.
        cpf_limpo = ''.join(filter(str.isdigit, cpf)) # Resulta em '12345678901'
        
        # Criação do Objeto no Banco de Dados
        # -----------------------------------
        # Usa o manager 'objects' do modelo Colaborador para criar um novo registro.
        # Colaborador.objects.create(...) é um atalho que cria e salva o objeto em um passo.
        # Os argumentos (nome_completo=nome, etc.) mapeiam os valores das variáveis Python
        # para os campos correspondentes definidos no models.py.
        Colaborador.objects.create(
            nome_completo=nome,
            cpf=cpf_limpo, # Salva o CPF limpo
            funcao=funcao,
            status=status
            # O campo 'data_cadastro' (se existir no modelo com auto_now_add=True) 
            # será preenchido automaticamente pelo Django.
        )
        # Redirecionamento após Salvar
        # ---------------------------
        # Após salvar com sucesso, redireciona o usuário para a URL nomeada 'index' 
        # (que é a página de lista). Isso evita que o usuário reenvie o formulário 
        # acidentalmente ao recarregar a página (Padrão Post/Redirect/Get).
        return redirect('index')

    # Se o método NÃO for POST (ou seja, é um GET, o usuário apenas acessou a página de cadastro)
    # -----------------------------------------------------------------------------------------
    # Simplesmente renderiza o template 'cadastro.html'. 
    # Não é necessário passar um contexto aqui, pois é um formulário vazio.
    return render(request, 'cadastro.html')


# View (Função) para a página de EDIÇÃO de Colaboradores (reutiliza cadastro.html)
# ==============================================================================
# Esta função é chamada para URLs como '/editar/1/', '/editar/5/', etc.
# O parâmetro 'id' vem da URL (definido como <int:id> no urls.py).
def colaborador_editar(request, id):
    # Busca do Objeto a Editar
    # -------------------------
    # Tenta encontrar um objeto Colaborador cujo 'id' (chave primária) seja igual ao 'id' 
    # recebido da URL. Se nenhum colaborador com esse ID for encontrado, a função 
    # 'get_object_or_404' automaticamente retorna uma página de erro 404.
    colaborador = get_object_or_404(Colaborador, id=id)

    # Verifica se o formulário de edição foi enviado (método POST).
    if request.method == 'POST':
        # Atualização dos Atributos do Objeto
        # ----------------------------------
        # Pega os novos dados enviados pelo formulário usando request.POST.get(...).
        # ATUALIZA diretamente os atributos do objeto 'colaborador' que já foi buscado do banco.
        colaborador.nome_completo = request.POST.get('nome_completo')
        colaborador.cpf = ''.join(filter(str.isdigit, request.POST.get('cpf'))) # Limpa o CPF
        colaborador.funcao = request.POST.get('funcao')
        colaborador.status = request.POST.get('status')
        
        # Salvar as Alterações no Banco
        # -----------------------------
        # Chama o método .save() no objeto 'colaborador'. O Django detecta que este 
        # objeto já existe no banco (porque tem um ID) e executa um comando SQL UPDATE 
        # em vez de um INSERT.
        colaborador.save()
        
        # Redireciona para a lista após salvar as alterações.
        return redirect('index')

    # Se o método for GET (o usuário apenas acessou a página de edição)
    # ----------------------------------------------------------------
    # Prepara o contexto para enviar o objeto 'colaborador' (com os dados atuais) para o template.
    context = {
        # A chave 'colaborador' no contexto permite acessar os dados no HTML 
        # (ex: {{ colaborador.nome_completo }}).
        'colaborador': colaborador 
    }
    # Reutiliza o mesmo template 'cadastro.html'. O template usará a variável 'colaborador' 
    # do contexto para preencher os campos do formulário (ver os 'value="..."' no HTML).
    return render(request, 'cadastro.html', context)


# View (Função) para EXCLUIR um Colaborador
# =========================================
# Esta função é chamada para URLs como '/excluir/1/', '/excluir/5/', etc.
# O parâmetro 'id' vem da URL.
def colaborador_excluir(request, id):
    # Busca do Objeto a Excluir
    # -------------------------
    # Encontra o colaborador pelo ID. Se não achar, retorna 404.
    colaborador = get_object_or_404(Colaborador, id=id)
    
    # Exclusão do Objeto do Banco
    # ---------------------------
    # Chama o método .delete() no objeto 'colaborador'. O Django executa o comando 
    # SQL DELETE correspondente para remover este registro do banco de dados.
    colaborador.delete()
    
    # Redirecionamento para a Lista
    # -----------------------------
    # Após excluir, redireciona o usuário de volta para a página de lista ('index').
    return redirect('index')