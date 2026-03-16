#  py L:/Python/execute_speed_test_1.py

import time

ct_num = int(100)
i = 1

while i < ct_num:
  print(str(int(time.time() * 1000)))
  i = i + 1