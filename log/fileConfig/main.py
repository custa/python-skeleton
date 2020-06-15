import logging
import logging.config
import foo

logging.config.fileConfig('logging.conf')

logger = logging.getLogger(__name__)
logger.info("main.py")

foo.foo()
