import time
import threading
import sys
import signal


def loop():
    for i in range(10000):
        time.sleep(1)
        print("loop(): %d" % i)


def handler1(signum, frame):
    print("handler1", signum)
    sys.exit(-1)


def handler2(signum, frame):
    print("handler2", signum)
    sys.exit(-1)


if __name__ == "__main__":
    t = threading.Thread(target=loop)
    t.start()
    signal.signal(signal.SIGTERM, handler1)
    signal.signal(signal.SIGINT, handler2)
