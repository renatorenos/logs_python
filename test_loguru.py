from loguru import logger
import sys

#configura o que irá mostar no console
logger.configure(handlers=[{"sink": sys.stderr, "level": "WARNING"}])

# Configuração para salvar todos os níveis de log em um arquivo
logger.add("log/log.log", level="DEBUG", rotation="500 MB")

# Exemplos de uso do logger
logger.debug("Isso será salvo apenas no arquivo.")
logger.info("Isso será salvo apenas no arquivo.")
logger.warning("Isso será salvo no arquivo e exibido no console.")
logger.error("Isso será salvo no arquivo e exibido no console.")
logger.critical("Isso será salvo no arquivo e exibido no console.")