import os


# 1 Pegar nome do arquivo
# 2 Pegar extensão do arquivo para determinar o tipo
# 3 Criar pastas: Imagens, Audios, Documentos, Vídeos, Outros
# 4 Mover arquivos para as pastas correspondentes

audios_ext = ['.mp3','.wav','.ogg']
videos_ext = ['.mp4','.mov','.avi','.mpeg','.mkv']
imagens_ext = ['.jpg','.jpeg','.png']
documentos_ext = ['.txt','.log','.pdf','.doc','.docx','.xls','.ocd']

def organizar(diretorio):
    AUDIO_DIR = os.path.join(diretorio, "Áudios")
    IMAGENS_DIR = os.path.join(diretorio, "Imagens")
    DOCUMENTOS_DIR = os.path.join(diretorio, "Documentos")
    VIDEOS_DIR = os.path.join(diretorio, "Vídeos")
    OUTROS_DIR = os.path.join(diretorio, "Outros")

    if not os.path.isdir(AUDIO_DIR):
        os.mkdir(AUDIO_DIR)
    if not os.path.isdir(IMAGENS_DIR):
        os.mkdir(IMAGENS_DIR)
    if not os.path.isdir(DOCUMENTOS_DIR):
        os.mkdir(DOCUMENTOS_DIR)
    if not os.path.isdir(VIDEOS_DIR):
        os.mkdir(VIDEOS_DIR)
    if not os.path.isdir(OUTROS_DIR):
        os.mkdir(OUTROS_DIR)

    nomes_arquivos = os.listdir(diretorio)

    nova_pasta = ''
    for arquivo in nomes_arquivos:
        if os.path.isdir(os.path.join(diretorio,arquivo)):
            pass
        else:
            #Extensao do arquivo com letras minúsculas
            extensao = str.lower(pegar_extensao(arquivo))
            print(arquivo, extensao)
            if extensao in audios_ext:
                nova_pasta = AUDIO_DIR
            elif extensao in videos_ext:
                nova_pasta = VIDEOS_DIR
            elif extensao in imagens_ext:
                nova_pasta = IMAGENS_DIR
            elif extensao in documentos_ext:
                nova_pasta = DOCUMENTOS_DIR
            else:
                nova_pasta = OUTROS_DIR
            # Move o arquivo para a pasta correspondente
            velho = os.path.join(diretorio, arquivo)
            novo = os.path.join(nova_pasta, arquivo)
            os.rename(velho, novo)
            print(f"Moveu: {velho} -> {novo}")


def pegar_extensao(nome_arquivo):
    indice = nome_arquivo.rfind('.')
    return nome_arquivo[indice:]

if __name__ == '__main__':
    organizar(os.path.join('/home/victor/Downloads'))