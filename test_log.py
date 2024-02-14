from logging import basicConfig #configuração 
from logging import DEBUG, WARNING # niveis
from logging import debug, info, error, critical, warning #chamadas
from logging import FileHandler, StreamHandler #handlers
from logging import Formatter

# formater_file_handler = Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler = FileHandler('log/app.log', 'a')
# file_handler.setLevel(WARNING)
# file_handler.setFormatter(formater_file_handler)

stream_handler = StreamHandler()
stream_handler.setLevel(WARNING)

basicConfig(
    level=DEBUG,
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        FileHandler('log/app.log', 'a'), #escreve no arquivo
        stream_handler#escreve no terminal
    ]
)

debug("mensagem de debug")
info("mensagem de info")
warning("mensagem de warning")
error("mensagem de error")
critical("mensagem critica")