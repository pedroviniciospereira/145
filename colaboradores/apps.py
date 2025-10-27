# Importa a classe base 'AppConfig' do Django, necessária para configurar um aplicativo.
from django.apps import AppConfig

# Define uma classe de configuração específica para o aplicativo 'colaboradores'.
# O Django usa esta classe para saber como o aplicativo deve se comportar e 
# como ele se integra ao projeto. O nome da classe geralmente segue o padrão 
# NomeDoAppConfig (PascalCase).
class ColaboradoresConfig(AppConfig):
    # [CONFIGURAÇÃO PADRÃO] Define o tipo de campo padrão a ser usado para chaves primárias 
    # (IDs) que o Django cria automaticamente nos modelos deste aplicativo, se um 
    # campo de chave primária não for explicitamente definido.
    # 'BigAutoField' corresponde a um inteiro grande de 64 bits (BIGINT no SQL), 
    # que é o recomendado para evitar problemas de limite de ID em tabelas grandes.
    default_auto_field = "django.db.models.BigAutoField"
    
    # [IMPORTANTE] Define o nome Python completo do aplicativo. 
    # É como o Django identifica este aplicativo internamente. 
    # Deve corresponder ao nome da pasta do seu aplicativo ('colaboradores').
    name = "colaboradores"
    
    # [NOTA] Geralmente, você não precisa modificar muito este arquivo, a menos que 
    # precise adicionar configurações específicas do aplicativo, como sinais (signals) 
    # ou tarefas de inicialização. Ele é registrado automaticamente no settings.py 
    # quando você adiciona 'colaboradores' a INSTALLED_APPS.