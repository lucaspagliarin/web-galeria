import os.path

from django.conf import settings
from pathlib import Path
from PIL import Image

def salva_imagens(filtros):
    imagens = filtros['imagens']
    project_path = settings.BASE_DIR
    project_path = project_path.parent.as_posix()
    path = '/webgaleria/galeria/arquivos/imagens/'
    for imagem in imagens:
        nome_arquivo = imagem.name
        caminho_completo = Path(project_path + path + nome_arquivo)
        img = Image.open(imagem.file)
        img = img.save(caminho_completo)

