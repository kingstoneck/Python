#  py L:\Python\time_test.py


import time
import datetime as dt
from datetime import datetime


cur_time = time.time() * 1000
print(cur_time)

dt = (datetime.fromtimestamp(time.time())).strftime('%H:%M:%S')

print(dt)


def current_time():
  time_now = (datetime.fromtimestamp(time.time())).strftime('%H:%M:%S')
  
  return time_now

def current_time_format():
  time_format_1 = (datetime.fromtimestamp(time.time())).strftime('%m%d%y%H%M%S%f')[:-3]
  return time_format_1

iter_num = 0

while iter_num < 10:   
  ct_now = current_time()
  ct_now_f1 = current_time_format()
  print(ct_now)
  print(ct_now_f1)
  time.sleep(1)
  iter_num += 1