import logging
import foo

logging.basicConfig(
    format="%(asctime)s %(filename)s:%(lineno)d [%(levelname)s] %(message)s",
    level=logging.INFO)

logger = logging.getLogger(__name__)
logger.info("main.py")

foo.foo()
