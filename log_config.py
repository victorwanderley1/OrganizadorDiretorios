import logging

# Configurar um manipulador de arquivo para o arquivo de log
log_file = "log_jobs.log"
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)

# Configurar um manipulador de console para exibir mensagens no console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Configurar um formato para as mensagens de log
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Configurar o nível de log global
logging.basicConfig(level=logging.INFO, handlers=[file_handler, console_handler])