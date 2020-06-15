import format
import time


print("%(asctime)s {}|%(name)s|%(threadName)s|%(filename)s:%(lineno)d|%(levelname)s|%(message)s"
      .format(time.strftime("%z")))

print("{:02}".format(1))
