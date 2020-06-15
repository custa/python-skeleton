import logging
import ssl
import sys
import time
import nsq
import tornado
import threading
import signal

logging.basicConfig(
    level=logging.INFO,
    format=
    "%(asctime)s {}|%(name)s|%(threadName)s|%(filename)s:%(lineno)d|%(levelname)s|%(message)s"
    .format(time.strftime("%z")))

logger = logging.getLogger(__name__)


def process_thread(message):
    time.sleep(1)
    logger.info("Process: %s(attempts: %s) -- %s", message.id,
                message.attempts, message.body)


count = 0


def handler(message):
    global count
    count += 1
    logger.info("receive: %s(attempts: %s) -- %s, count: %d", message.id,
                message.attempts, message.body, count)
    time.sleep(0.01)
    message.finish()
    # message.enable_async()
    #
    # def finish(none):
    #     logger.info(
    #         "Finish(): %s(attempts: %s)",
    #         message.id,
    #         message.attempts)
    #     message.finish()
    #
    # loop = tornado.ioloop.IOLoop.current()
    # future = loop.run_in_executor(None, process_thread, message)
    # loop.add_future(future, finish)


def loop():
    for i in range(10):
        time.sleep(1)
        logger.info("loop(): %d" % i)


if __name__ == "__main__":
    opts = {
        "cert_reqs": ssl.CERT_REQUIRED,
        "keyfile": "../client-key.pem",
        "certfile": "../client-cert.pem",
        "ca_certs": "../ca-cert.pem",
    }
    r = nsq.Reader(message_handler=handler,
                   nsqd_tcp_addresses=["10.77.134.33:4150"],
                   topic="topic#ephemeral",
                   channel="channel#ephemeral",
                   tls_v1=True,
                   tls_options=opts,
                   max_tries=2,
                   max_in_flight=10,
                   max_backoff_duration=sys.float_info.min,
                   lookupd_poll_interval=1)

    threading.Thread(target=loop).start()
    nsq.run()
    print("hello")
