# -*- coding:utf-8 -*-
"""
$ time python main.py

real    0m34.561s
user    0m29.003s
sys     0m5.548s
$ time python3 main.py

real    0m25.530s
user    0m25.518s
sys     0m0.003s

"""

N = int(1e9)
# python2 range 语句会分配大量内存
for i in range(N):
    0 + 0
