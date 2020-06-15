import logging


logging.info("before invoke basicConfig")
logging.warning("before invoke basicConfig")

# 调用写日志接口之后再调用 basicConfig 无效
# https://docs.python.org/3.7/library/logging.html#logging.basicConfig
# The functions debug(), info(), warning(), error() and critical() will call basicConfig()
# automatically if no handlers are defined for the root logger.

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s|%(levelname)s|%(message)s"
                    )

logging.info("after invoke basicConfig")
logging.warning("after invoke basicConfig")
