import time

secs = 1573806273.000655
lt = time.localtime(secs)

print(time.strftime("%F %T %z", lt))
