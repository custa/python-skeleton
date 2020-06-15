from queue import Queue
import threading
import time

cameras = ["a", "b"]


def handler(q):
    name = threading.current_thread().name
    while True:
        m = q.get()
        if m is None:
            print("thread %s break" % name)
            break
        print("thread %s receive: %s" % (name, m))
        time.sleep(0.1)


queues = {}
threads = {}
for i in range(len(cameras)):
    name = cameras[i]
    q = Queue(10)
    queues[name] = q
    t = threading.Thread(target=handler, args=(q, ), name=name)
    t.start()
    threads[name] = t

for i in range(20):
    for t in threads:
        try:
            queues[t].put(i, block=False)
        except Exception as e:
            print("drop: %d for %s" % (i, t))
