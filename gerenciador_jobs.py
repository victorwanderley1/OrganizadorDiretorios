import schedule
import organizacao as org
import logging
import log_config
import time

if __name__ == "__main__":
    logging.info("Iniciando Gerenciador Jobs")
    job1 = schedule.every().hour.at(':15').do(org.organizar_pastas, diretorio='/home/victor/Downloads')
    while True:
        try:
            schedule.run_pending()
        except Exception as e:
            logging.warning(e)