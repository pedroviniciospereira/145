# Importa o módulo 'models' do Django, que contém as classes e funções 
# necessárias para definir modelos de banco de dados.
from django.db import models

# Define uma nova classe chamada 'Colaborador'.
# Herdar de 'models.Model' transforma esta classe Python comum 
# em um Modelo Django, que o ORM (Object-Relational Mapper) do Django usará 
# para interagir com a tabela correspondente no banco de dados 
# (por padrão, a tabela será nomeada 'colaboradores_colaborador').
class Colaborador(models.Model):
    # Define um campo chamado 'nome_completo' no modelo.
    # models.CharField cria uma coluna do tipo VARCHAR no banco de dados.
    #   - max_length=150: Define o tamanho máximo da string que pode ser armazenada 
    #     nesta coluna (obrigatório para CharField).
    nome_completo = models.CharField(max_length=150)
    
    # Define um campo 'cpf'.
    # models.CharField armazena o CPF como texto.
    #   - max_length=11: Define o tamanho (considerando que salvamos o CPF sem pontos/traço).
    #   - unique=True: [IMPORTANTE] Garante que não possam existir dois colaboradores 
    #     com o mesmo CPF no banco de dados. O banco aplicará uma restrição UNIQUE.
    cpf = models.CharField(max_length=11, unique=True)
    
    # Define um campo 'funcao'.
    # models.CharField para armazenar a função/cargo do colaborador.
    funcao = models.CharField(max_length=50)

    # [BOA PRÁTICA] Define uma lista de tuplas para as opções do campo 'status'.
    # Cada tupla contém: (valor_armazenado_no_banco, valor_exibido_para_usuario).
    # Isso melhora a consistência e facilita a manutenção.
    STATUS_CHOICES = [
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
    ]
    # Define um campo 'status'.
    # models.CharField para armazenar o status.
    #   - max_length=10: Tamanho suficiente para 'Ativo' ou 'Inativo'.
    #   - choices=STATUS_CHOICES: Vincula este campo às opções definidas acima. 
    #     No Django Admin e em ModelForms, isso renderizará um campo <select> automaticamente.
    #   - default='Ativo': Define o valor padrão para este campo se nenhum valor for 
    #     fornecido ao criar um novo Colaborador.
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Ativo')

    # Define um campo 'data_cadastro'.
    # models.DateTimeField armazena data e hora.
    #   - auto_now_add=True: [IMPORTANTE] Faz com que o Django preencha automaticamente 
    #     este campo com a data e hora exatas do momento em que o objeto Colaborador 
    #     é CRIADO pela primeira vez. O campo não será atualizado depois.
    data_cadastro = models.DateTimeField(auto_now_add=True)

    # [BOA PRÁTICA] Define o método especial '__str__'.
    # Este método retorna uma representação em string "legível" do objeto Colaborador.
    # É o que o Django Admin (e outras partes do Django) usa para exibir o objeto.
    # Aqui, ele retorna o nome completo do colaborador.
    def __str__(self):
        return self.nome_completo