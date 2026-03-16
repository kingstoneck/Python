#  py L:\Python\sscursor_test.py


import time
from datetime import datetime


cur_time = time.time() * 1000
print(cur_time)

dt = (datetime.fromtimestamp(time.time())).strftime('%H:%M:%S')

print(dt)