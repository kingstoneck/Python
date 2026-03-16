# py L:/Python/JSON_Read_Write_8.py

import sys
import time
import json
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

#
#Need to enable a reconnect loop if the mysql connection drops
#Need to write to error file if the mysql connection fails so we do not lose data
#
#
#this program needs to read a new row from the raw data, find the cooresponding second and minute dataset and create it
# if it does not exist, read the current data, sum the old data and new data, calculate the indicators, and write to file
#
#Need to have the program check to make sure the SQL connection is open, and reopen if it is closed
#
#See text at bottom for an example of auto-commit for SQL from stack overflow

row_id = int(0)
#line_details = []

try:
  connection = mysql.connector.connect(host='127.0.0.1',
                                       database='stonks_test_1',
                                       user='test',
                                       password='Testing123!')

  cursor = connection.cursor()
      
  sql_row_select = """select * from tsla_test_3 where index = %s"""
  row_data = (
  cursor.execute(sql_row_select, (row_id,))
  
  connection.commit()      
  cursor.close()
  row_id = row_id + 1      
      
      
      
      
#   with open(data_file4, 'r') as tsla_data:
#    for line in tsla_data:     
#      line_details = json.loads(line)[0]
#      timestamp = line_details.get('ts', "NULL")
#      #str(int(time.time() * 1000))
#      #timestamp = line_details.get('ts', "NULL")
#      event = line_details.get('ev', "NULL")
#      status = line_details.get('status', "NULL")
#      message = line_details.get('message', "NULL")
#      trade_symbol = line_details.get('sym', "NULL")
#      trade_id = line_details.get('i', "NULL")
#      exchange_id = line_details.get('x', "NULL")
#      price = line_details.get('p', "NULL")
#      volume = line_details.get('s', "NULL")
#      condition = line_details.get('c', "NULL")
#      trade_time = line_details.get('t', "NULL")
#      tape = line_details.get('z', "NULL")
#      
#      sql_insert = "INSERT INTO tsla_test_3 (ts, ev, status, msg, sym, i, x, p, s, c, t, z) " "VALUES (%s, %s, '%s', '%s', '%s', %s, %s, %s, %s, '%s', %s, %s)" % (timestamp, event, status, message, trade_symbol, trade_id, exchange_id, price, volume, condition, trade_time, tape)
#      cursor = connection.cursor()
#      cursor.execute(sql_insert)
#      connection.commit()
#      print("ts:",timestamp, ",",event, ",",status, ",",message, ",", trade_symbol, ",", trade_id, ",",
#            exchange_id, ",", price, ",", volume, ",", condition, ",", trade_time, ",", tape)
#      print(cursor.rowcount, "Record inserted successfully into tsla_test_3 table")
#      cursor.close()
      
except mysql.connector.Error as error:
  print("Failed to insert record into tsla_test_3 table {}".format(error))
      
finally:
  if (connection.is_connected()):
    connection.close()
    print("MySQL connection is closed")
    
    
#https://stackoverflow.com/questions/24415699/get-updated-mysql-table-entries-in-python-without-closing-connection
#    
#...for the "reading" script would be to enable autocommit mode by calling db.autocommit(True) after opening the connection. 
#The Python database API specifies that "if the database supports an auto-commit feature, this must be initially off," but 
#there's no reason you can't turn it on if you're not worried about concurrency issues, which should be the case for your 
#"reading" script.
#
#In fact, if these two scripts are the only things going on with the server, and you don't need transactions in your other script,
# the simplest thing to do would be to turn autocommit on in both scripts and forget about it. But this has the potential
# to bite you in the ass later on if you forget what you did here and go write other scripts that need to perform
# concurrent transactions.
#
#*Note that the cursor created for you by db.__enter__() is not closed by db.__exit__(). In this case, 
#MySQLdb.Cursor is actually just a Python object that emulates a cursor; it doesn't tie up any additional server resources, 
#and you generally don't have to worry about closing it. 
#In fact, you can continue to refer to a Cursor object by whatever name you bound it to in the with statement 
#after the with block exits, so long as its parent Connection remains open. (Unless, of course, you explicitly close() the cursor
#or bind its name to another object.)    

