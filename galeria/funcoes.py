import os.path

from django.conf import settings
from pathlib import Path
# from PIL import Image
from django.contrib.auth.models import User
from _datetime import datetime

def salva_imagens(dados):
    try:
        imagens = dados['imagens']
        project_path = settings.BASE_DIR
        project_path = project_path.parent.as_posix()
        path = '/webgaleria/galeria/arquivos/imagens/'
        for imagem in imagens:
            nome_arquivo = imagem.name
            caminho_completo = Path(project_path + path + nome_arquivo)
            # img = Image.open(imagem.file)
            # img = img.save(caminho_completo)

        return True
    except:
        return False


def cria_usuario(dados):
    pode_criar = False
    try:
        busca = User.objects.get(username=dados['username'])
        return {'erro': True, 'mensagem': 'O username ' + dados['username'] + ' não está disponível!', 'cadastrar': True}
    except:
        try:
            busca = User.objects.get(email=dados['email'])
            return {'erro': True, 'mensagem': 'Email já cadastrado!', 'cadastrar': True}
        except:
            pode_criar = True

    try:
        if pode_criar:
            user = User.objects.create_user(dados['username'], dados['email'], dados['password'],
                                            first_name=dados['first_name'], last_name=dados['last_name'], is_active=True,
                                            is_staff=False, is_superuser=False, date_joined=datetime.now())
            return {'sucesso': True}
    except:
        return {'erro': True, 'mensagem': 'Ocorreu um erro inesperado. Parece que estamos tendo dificuldades para crair seu usuário', 'cadastrar': True}
