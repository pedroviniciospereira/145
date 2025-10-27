# PROJETIC_EPI: Sistema de Gerenciamento de EPIs 👷🚧

## Visão Geral

Este projeto é um Sistema Web para Gerenciamento de Equipamentos de Proteção Individual (EPIs), desenvolvido como parte do curso Técnico em Desenvolvimento de Sistemas. O objetivo é atender à necessidade de uma construtora fictícia que busca melhorar o controle e assegurar o uso de EPIs por seus colaboradores, solucionando problemas identificados em auditorias internas e aumentando a segurança no ambiente de trabalho.

O sistema visa controlar o empréstimo e devolução de EPIs para cada funcionário, permitindo um gerenciamento mais eficaz e auxiliando na conformidade com as normas regulamentadoras.

## Funcionalidades Implementadas (Etapa 2)

* Cadastro de Colaboradores (Create): Permite adicionar novos funcionários ao sistema.
* Listagem de Colaboradores (Read): Exibe todos os colaboradores cadastrados, com informações básicas e status. Inclui:
    * Cards com estatísticas (Total, Ativos, Inativos).
    * Barra de pesquisa por Nome, CPF ou Função.
* Atualização de Colaboradores (Update): Permite editar os dados de um colaborador existente.
* Exclusão de Colaboradores (Delete): Permite remover um colaborador do sistema.
* Persistência de Dados: Todos os dados dos colaboradores são salvos em um banco de dados SQLite.
* Interface Intuitiva: Design baseado nos wireframes fornecidos, com foco em usabilidade.
* Máscara de CPF: Validação no frontend para o formato do CPF.

## Funcionalidades Planejadas (Próximas Etapas)

* Conforme for sendo pedido será sendo adicionado....

## Tecnologias Utilizadas 🛠️

* Backend: Python, Django 
* Frontend: HTML, CSS, JavaScript
* Banco de Dados: SQLite 3 (para desenvolvimento)
* Controle de Versão: Git, GitHub

## Configuração e Execução do Projeto 🚀

Siga os passos abaixo para configurar e rodar o projeto localmente:

1.  Pré-requisitos:
    * Python 3.8 ou superior instalado.
    * Git instalado.

2.  Clone o Repositório:**
    ```bash
    git clone [https://github.com/pedroviniciospereira/PROJETIC_EPI.git](https://github.com/pedroviniciospereira/PROJETIC_EPI.git)
    cd PROJETIC_EPI
    ```

3.  Crie e Ative um Ambiente Virtual:
    * No Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * No macOS/Linux:
        ```bash
        python -m venv venv
        source venv/bin/activate
        ```
    *(Você verá `(venv)` no início do seu terminal se a ativação funcionou).*

4.  Instale as Dependências:
    *(Certifique-se de que o ambiente virtual esteja ativo)*
    ```bash
    pip install django
    ```
    *(Opcional: Se existir um arquivo `requirements.txt`, use `pip install -r requirements.txt`)*

5.  Aplique as Migrações do Banco de Dados:
    Este comando cria as tabelas necessárias no arquivo `db.sqlite3`.
    ```bash
    python manage.py migrate
    ```

6.  (Opcional) Crie um Superusuário:
    Para acessar o painel de administração do Django (`/admin/`).
    ```bash
    python manage.py createsuperuser
    ```
    *(Siga as instruções para definir nome de usuário, email e senha).*

7.  *Execute o Servidor de Desenvolvimento:
    * Para acesso local padrão:
        ```bash
        python manage.py runserver
        ```
    * Importante (Codespaces/Ambientes Remotos):** Use `0.0.0.0` para permitir conexões externas:
        ```bash
        python manage.py runserver 0.0.0.0:8000
        ```

8.  Acesse o Sistema:
    Abra seu navegador e acesse `http://127.0.0.1:8000/` (ou o endereço fornecido pelo Codespace).

## Pesquisa sobre Dockerfile 🐳

Conforme solicitado na Etapa 2, foi realizada uma pesquisa sobre a integração de um `Dockerfile` ao projeto. Um Dockerfile permitiria "empacotar" a aplicação Django e suas dependências (Python, bibliotecas) em uma imagem de contêiner. Isso garante que o ambiente de execução seja consistente em diferentes máquinas (desenvolvimento, teste, produção), facilitando o deploy e evitando problemas de "na minha máquina funciona". A criação e integração do Dockerfile pode ser uma etapa futura do projeto.
