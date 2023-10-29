import logging
import os
import log_config

AUDIO_EXT = ["mp3","wav","flac","aac","ogg","m4a","wma","aiff","ape","midi",
                "amr","ac3","dts","ra"]

VIDEO_EXT = ["mp4", "avi", "mkv", "mov", "wmv", "flv", "webm", "mpeg", "3gp",
             "rmvb", "m4v", "mpg", "divx", "ts", "vob", "swf"]

IMAGEM_EXT = ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "raw", "svg", "ico",
    "webp", "heif", "pcx", "eps", "psd", "ai", "indd"]

DOCUMENTO_EXT = ["doc", "docx", "txt", "rtf", "pdf", "odt", "xls", "xlsx", "csv", "ppt",
    "pptx", "pps", "odp", "html", "xml", "json", "yaml", "md", "log"]

SCRIPT_EXT = ["c", "cpp", "h", "hpp", "java", "py", "js", "html", "css",
                    "php", "asp", "rb", "pl", "go", "swift", "sql", "xml", "json",
                    "yaml", "md", "sh"]
def identificar_diretorio(diretorio):
    return os.path.isdir(os.path.abspath(diretorio))

def criar_pastas(diretorio):
    diretorios_pastas = get_diretorios_pastas(diretorio)
    logging.info("Verificando pastas")
    for pasta in diretorios_pastas:
        if not identificar_diretorio(pasta):
            logging.info(f"Criando pasta: {pasta}")
            os.mkdir(pasta)

def get_diretorios_pastas(diretorio):
    AUDIO_DIR = os.path.abspath(os.path.join(diretorio, "Áudios"))
    VIDEO_DIR = os.path.abspath(os.path.join(diretorio, "Vídeos"))
    IMAGEM_DIR = os.path.abspath(os.path.join(diretorio, "Imagens"))
    DOCUMENTOS_DIR = os.path.abspath(os.path.join(diretorio, "Documentos"))
    SCRIPTS_DIR = os.path.abspath(os.path.join(diretorio, "Scripts"))
    OUTROS_DIR = os.path.abspath(os.path.join(diretorio, "Outros"))
    return [AUDIO_DIR, VIDEO_DIR, IMAGEM_DIR, DOCUMENTOS_DIR, SCRIPTS_DIR, OUTROS_DIR]

def get_extensao_arquivo(arquivo):
    return str.split(arquivo, '.')[-1]

def mover_arquivo(arquivo, diretorio_origem, diretorio_destino):
    origem = os.path.join(diretorio_origem,arquivo)
    destino = os.path.join(diretorio_destino,arquivo)
    logging.info(f"Movendo: {origem} -> {destino}")
    #Comentado até estar pronto
    os.rename(origem,destino)


def organizar_pastas(diretorio):
    logging.info("Iniciando Execução: Organização de Pasta")
    diretorio_absoluto_raiz = os.path.abspath(diretorio)
    list_arquivos = os.listdir(diretorio_absoluto_raiz)
    criar_pastas(diretorio_absoluto_raiz)
    pastas = get_diretorios_pastas(diretorio_absoluto_raiz)

    for arquivo in list_arquivos:
        if not identificar_diretorio(os.path.join(diretorio,arquivo)):
            extensao = get_extensao_arquivo(arquivo)
            if extensao in AUDIO_EXT:
                mover_arquivo(arquivo,diretorio,pastas[0])
            elif extensao in VIDEO_EXT:
                mover_arquivo(arquivo,diretorio,pastas[1])
            elif extensao in IMAGEM_EXT:
                mover_arquivo(arquivo,diretorio,pastas[2])
            elif extensao in DOCUMENTO_EXT:
                mover_arquivo(arquivo,diretorio,pastas[3])
            elif extensao in SCRIPT_EXT:
                mover_arquivo(arquivo,diretorio,pastas[4])
            else:
                mover_arquivo(arquivo,diretorio,pastas[5])
    logging.info("Finalizando Execução: Organização de Pasta")

if __name__ == "__main__":
    organizar_pastas('.')