import logging.handlers
import time


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s {}|%(name)s|%(threadName)s|%(filename)s:%(lineno)d|%(levelname)s|%(message)s"
    .format(time.strftime("%z")),
    handlers=[
        logging.handlers.RotatingFileHandler(
            "wtf.log",
            maxBytes=(1024 * 1),
            backupCount=7,
            encoding='utf-8'
        ),
        logging.StreamHandler()
    ])

for i in range(10):
    logging.info("hello")

logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything
