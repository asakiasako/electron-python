import logging
import logging.handlers
from .config import LOG_FILE_PATH, LOG_FILE_BACKUP_COUNT
from os.path import join

# logger
rpcServerLogger = logging.getLogger('RPCServer')
rpcServerLogger.setLevel(logging.DEBUG)
# handler
filename = 'RPC-Server.log'
fileHandler = logging.handlers.TimedRotatingFileHandler(join(LOG_FILE_PATH, filename) , 'midnight', 1, LOG_FILE_BACKUP_COUNT)
# formatter
appLogFormatter = logging.Formatter(fmt='\n[%(asctime)s - %(name)s - %(levelname)s - %(message)s]')

fileHandler.setFormatter(appLogFormatter)
rpcServerLogger.addHandler(fileHandler)