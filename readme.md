# Instalação do Projeto

## Requisitos Mínimos


## Passo-a-Passo

Para fazer um clone do projeto na sua máquina, utilizaremos o Git.
Estaremos utilizando o <b>Git Bash</b> como terminal nesse projeto. 

1) Rode o seguinte comando na pasta raíz de projetos: 

    <code>
        git clone https://github.com/lucaspagliarin/web-galeria.git
    </code>
<br/>

2) Acesse o repositório do projeto utilizando o comando:

    <code>
        cd web-galeria
    </code>
<br/>

3. Para utilizar o Virtual Environment do Python, vamos executar o seguinte comando:

    <code>
    source myvenv/bin/activate
    </code>
    
    *Note que este comando pode variar conforme o tipo de terminal e o sistema operacional que você estiver utilizando*
<br/>

    Você irá notar que agora no seu terminal, existe um <code>(myvenv)</code> antes do caminho atual.  

4) Para Instalar os requisitos necessários para executar a aplicação, execute o seguinte comando:

    <code>
    pip install -r requirements.txt
    </code>

    Ele instalará as dependências do projeto no seu ambiente virtual.

<br/>

5) Finalmente, para rodar o projeto utilizaremos o comando:
    
    <code>
    python manage.py runserver
    </code>

<br/>


Pronto! O Projeto estará rodando na sua máquina simulando um servidor local.

Por padrão os projetos em Django rodam no endereço <code>http://127.0.0.1:8000/</code>, mas indicamos verificar o endereço utilizado no terminal.

# Funcionalidades

### Cadastro de Usuários e Login

Para acessar o sistema, o usuário precisará estar logado.

O usuário poderá realizar o seu cadastro, informando seu Usuário, e-mail e senha.

Deixamos um usuário padrão cadastrado com alguns dados. Seguem informações de login
    
    usuário: lucaspagliarin
    senha: 123

### Criação de Coleções


### Adição de Imagens nas Coleções


### Favoritar Imagens e Ver a Coleção de Favoritos
