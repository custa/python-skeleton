import logging

logger = logging.getLogger(__name__)

logger.warning("foo.py")


def foo():
    # 不会打印？
    logger.warning("foo()")
