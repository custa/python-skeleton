# -*- coding:utf-8 -*-

import os
from multiprocessing import Pool
"""
# python3 耗时是 python2 的两倍
[c00510494@euleros-gpu001 pool]$ time python cpu.py
Parent process 24773.
Waiting for all subprocesses done...
Run task 0 (24774)...
Run task 1 (24775)...
All subprocesses done.

real    0m1.821s
user    0m3.591s
sys     0m0.006s
[c00510494@euleros-gpu001 pool]$ time python3 cpu.py
Parent process 24863.
Waiting for all subprocesses done...
Run task 0 (24864)...
Run task 1 (24865)...
All subprocesses done.

real    0m3.242s
user    0m6.253s
sys     0m0.007s

"""


def cpu(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    N = int(1e8)
    i = 0
    while i < N:
        i += 1


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(2)
    for i in range(2):
        p.apply_async(cpu, args=(i, ))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
