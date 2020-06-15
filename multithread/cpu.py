# -*- coding:utf-8 -*-

import threading
"""
# python2 会占用 CPU 用于线程之间的调度，总占用超过 100%，造成使用多核并行处理的假象
$ time python cpu.py
thread MainThread is running...
cpu thread Thread-1 is running...
cpu thread Thread-2 is running...

real    0m7.117s
user    0m6.216s
sys     0m5.567s
$ time python3 cpu.py
thread MainThread is running...
cpu thread Thread-1 is running...
cpu thread Thread-2 is running...

real    0m6.276s
user    0m6.276s
sys     0m0.013s

"""


def cpu():
    print('cpu thread %s is running...' % threading.current_thread().name)
    N = int(1e8)
    i = 0
    while i < N:
        i += 1


print('thread %s is running...' % threading.current_thread().name)
n = 2
ts = []
for i in range(n):
    t = threading.Thread(target=cpu)
    t.start()
    ts.append(t)

for t in ts:
    t.join()
