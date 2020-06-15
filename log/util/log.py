import logging


def get_logger(name='root'):
    logger = logging.getLogger(name)
    return logger


logger = get_logger('root')
