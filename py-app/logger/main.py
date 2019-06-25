import logging
from ._types import SafeFileHandler

LOGGERS = {}

def register_logger(name, path, level=logging.DEBUG):
    # define logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    # define handler
    fileHandler = SafeFileHandler(path)
    # define formatter
    formatter = logging.Formatter(fmt='\n[%(asctime)s - %(name)s - %(levelname)s - %(message)s]')

    # set to logger
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    LOGGERS[name] = logger

    return logger

def get_logger(name):
    return LOGGERS[name]

def del_logger(name):
    del(LOGGERS[name])
