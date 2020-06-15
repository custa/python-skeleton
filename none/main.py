import time

a = []

N = 10000000

start = time.time()
for i in range(N):
    if a == []:
        None
end = time.time()
print("if a == []: {}".format((end - start)))

start = time.time()
for i in range(N):
    if len(a) == 0:
        None
end = time.time()
print("if len(a) == 0: {}".format((end - start)))
