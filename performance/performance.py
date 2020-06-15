"""
$ time python performance.py

real    0m4.535s
user    0m4.533s
sys     0m0.001s
$ time python3 performance.py

real    0m6.286s
user    0m6.282s
sys     0m0.004s
"""

N = int(1e8)
i = 0
while i < N:
    i += 1
