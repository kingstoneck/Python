# py L:/Python/Print_DB_1.py
#
#I added the ini file and broke the program.  Keep testing.

import configparser
#import MySQLdb.cursors
import mysql.connector
from mysql.connector import Error

config = configparser.ConfigParser()
config.read('L:/Python/restricted/testconfig.ini')

try:
  connection = mysql.connector.connect(host='127.0.0.1',
                                       database='sql_test_1',
                                       user='',
                                       password='')
  if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server v:", db_Info)
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connect to database: ", record)

except Error as error_log:
  print("Error while connecting to MySQL Database", error_log)
finally:
  if (connection.is_connected()):
    cursor.close()
    connection.close()
    print("MySQL connection is closed")
    
newtext = input("wait for a keyboard input")

  
#Old time write code
#
#import time
#
#num = int(input("Enter a natural number "))
#num=int(10)
#i=1
#
#with open("L:/Python/data/print_test_2.txt", 'a') as file1:
# file1.write("The numbers are as follows: \n")
# print("The numbers are as follows: \n")
#
#while i<=num:
# text1 = 'i=' + repr(i)
# with open("L:/Python/data/print_test_3.txt", 'a') as file1:
#  #file1.write("timestamp = ")
#  file1.write("timestamp = " + str(int(time.time() * 1000)) + ": " + text1 + "\n")
#  print("i=",i)
#  time.sleep(.001)
#  i=i+1