# Importa o módulo 'forms' do Django, que contém as classes e funcionalidades 
# para criar formulários HTML e validar dados.
from django import forms
# Importa o modelo 'Colaborador' do arquivo models.py deste mesmo app (indicado pelo '.').
from .models import Colaborador

# Define uma nova classe chamada 'ColaboradorForm'.
# Herdar de 'forms.ModelForm' é uma forma poderosa e conveniente de 
# criar um formulário que está diretamente ligado a um modelo Django ('Colaborador').
# O Django automaticamente cria os campos do formulário com base nos campos do modelo.
class ColaboradorForm(forms.ModelForm):
    
    # A classe interna 'Meta' é usada para fornecer informações sobre o ModelForm.
    class Meta:
        # 'model = Colaborador': Especifica qual modelo Django este formulário está associado.
        model = Colaborador
        # 'fields = [...]': Define quais campos do modelo 'Colaborador' devem ser incluídos 
        # neste formulário. O Django criará automaticamente os campos HTML correspondentes 
        # (CharField -> <input type="text">, CharField com choices -> <select>, etc.).
        fields = ['nome_completo', 'cpf', 'funcao', 'status']
        # Você também poderia usar 'exclude = [...]' para incluir todos os campos EXCETO alguns,
        # ou '__all__' para incluir todos os campos do modelo.

    # O método especial '__init__' é o construtor da classe. Ele é chamado quando 
    # uma instância do ColaboradorForm é criada (ex: form = ColaboradorForm()).
    # '*args' e '**kwargs' permitem que o construtor aceite qualquer número de 
    # argumentos posicionais e nomeados, respectivamente.
    def __init__(self, *args, **kwargs):
        # 'super().__init__(*args, **kwargs)': [IMPORTANTE] Chama o construtor da classe pai 
        # (forms.ModelForm). Isso garante que toda a inicialização padrão do ModelForm 
        # seja executada antes do nosso código personalizado.
        super().__init__(*args, **kwargs)
        
        # Personalização dos Widgets (Campos HTML)
        # ========================================
        # 'self.fields' é um dicionário que contém todos os campos definidos para este formulário.
        # A chave é o nome do campo (ex: 'nome_completo').
        # O valor é uma instância de um campo de formulário do Django (ex: forms.CharField).
        
        # 'self.fields['nome_completo'].widget': Acessa o "widget" associado ao campo 
        # 'nome_completo'. O widget é o responsável por renderizar o campo como HTML 
        # (neste caso, provavelmente um TextInput, que gera <input type="text">).
        
        # '.attrs': É um dicionário que contém os atributos HTML do widget (como id, class, placeholder).
        
        # '.update({'id': 'nome'})': Adiciona ou atualiza o atributo 'id' do widget HTML 
        # para ser 'nome'. Isso é útil para referenciar o campo no CSS ou JavaScript, 
        # ou para associar labels (<label for="nome">).
        self.fields['nome_completo'].widget.attrs.update({'id': 'nome'})
        # Faz o mesmo para o campo 'cpf', definindo seu ID HTML como 'cpf'.
        self.fields['cpf'].widget.attrs.update({'id': 'cpf'})
        # Define o ID HTML do campo 'funcao' como 'funcao'.
        self.fields['funcao'].widget.attrs.update({'id': 'funcao'})
        # Define o ID HTML do campo 'status' (que será renderizado como <select>) como 'status'.
        self.fields['status'].widget.attrs.update({'id': 'status'})
        
        # [NOTA] Embora este Form não esteja sendo usado ativamente na sua view 'colaborador_novo'
        # (que pega os dados diretamente do request.POST), ele é útil para validação automática
        # e seria essencial se você quisesse usar a renderização de formulário do Django 
        # com {{ form.as_p }} ou {{ form.nome_completo }}, etc., no template HTML.