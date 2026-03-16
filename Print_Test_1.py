#	py L:/Python/Print_Test_1.py

import time
from datetime import datetime, date, time

#ts = datetime.datetime.now().isoformat("_").split

def ts(fn, fmt='%Y.%m.%d.{fn}'):    #ts = time stamp, fn = file name
  #import datetime
  return datetime.datetaime.now().strftime(fmt).format(fn=fn)
  
fn = ts('Test_1.txt', '{fn}.%d.%m.%Y')

print(fn)

#num = int(input("Enter a natural number "))
#num=int(10)
#i=1
#
#with open("L:/Python/data/print_test_2.txt", 'a') as file1:
#  file1.write("The numbers are as follows: \n")
#  print("The numbers are as follows: \n")
#
#while i<=num:
#  text1 = 'i=' + repr(i)
#  with open("L:/Python/data/print_test_3.txt", 'a') as file1:
#    #file1.write("timestamp = ")
#    file1.write("timestamp = " + str(int(time.time() * 1000)) + ": " + text1 + "\n")
#    print("i=",i)
#    time.sleep(.01)
#    i=i+1