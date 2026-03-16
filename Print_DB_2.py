# py L:/Python/Print_DB_2.py
#
#I added the ini file and broke the program.  Keep testing.
#Check file 1 for previous code.

import configparser
import mysql.connector
from mysql.connector import Error, errorcode

config = configparser.ConfigParser()
config.read('L:/Python/restricted/testconfig.ini')

try:
    connection = mysql.connector.connect(host = config['sqltest']['host'],
                                         database = config['sqltest']['db'],
                                         user = config['sqltest']['usr'],
                                         password = config['sqltest']['pwd'])
    if connection.is_connected():
      db_Info = connection.get_server_info()
      print("Connected to MySQL Server v:", db_Info)
      cursor = connection.cursor()
      cursor.execute("select database();")
      record = cursor.fetchone()
      print("You're connected to database: ", record)

    mySql_insert_query = """INSERT INTO test_table_1 (Id, Name, Price, Date) 
                           VALUES 
                           (10, 'Lenovo ThinkPad P71', 6459, '2019-08-14') """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into test_table_1 table")
    cursor.close()

except Error as error_log:
  if error_log == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Connection error, incorrect username or password", error_log)
  elif error_log == errorcode.ER_BAD_DB_ERROR:
    print("MySQL Database does not exist", error_log)
  else:
    print(error_log)

finally:
  if 'connection' in locals():
    if (connection.is_connected()):
          #cursor.close()
          connection.close()
          print("MySQL connection is now closed")
  else:
    print("MySQL failed to open, ending program")

  
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