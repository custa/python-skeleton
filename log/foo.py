import logging

logger = logging.getLogger(__name__)

logger.warning("foo.py")


def foo():
    logger.info("foo()")
