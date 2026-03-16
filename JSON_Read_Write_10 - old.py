# py L:/Python/JSON_Read_Write_10.py

import sys
import time
import json
import functools
#import mysql.connector
from json import JSONDecoder
from functools import partial
#from mysql.connector import Error
#from mysql.connector import errorcode

#below is to define data checks.  Not needed, line_details.get() takes care of the check in 1 line
#def value_check(data, attribute, default_value):
#  return data.get(attribute) or NULL
#
#def json_check(data):
#  data_to = value_check(
#
#Need to read multiple objects in 1 line of json
#Need to nest define functions for connection
#Need to enable a reconnect loop if the mysql connection drops
#Need to write to error file if the mysql connection fails so we do not lose data
#

#chunk = []
#num = int()
#i=1
line_details = []
data_file1 = 'L:/aa_Stocks/Data/TSLA_05_26_20.txt'
data_file2 = 'L:/aa_Stocks/Data/TSLA_Test_Data_JSON_1.txt'
data_file3 = 'L:/aa_Stocks/Data/TSLA_Test_Data_JSON_2.txt'
data_file4 = 'L:/aa_Stocks/Data/Test_3_TSLA/TSLA_07_13_20_LE_format.txt'

data_file_use = data_file3
data_parse = data_file_use
data_read = data_file_use

def json_parse(fileobj, decoder=JSONDecoder(), buffersize=1024, delimiters=','):
  buffer = ''
  with open(data_parse, 'r') as file_obj:
    for chunk in iter(functools.partial(file_obj.read, buffersize), ''):
      buffer += chunk
      while buffer:
        try:
            stripped = buffer.strip(delimiters)
            result, index = decoder.raw_decode(stripped)
            yield result
            buffer = stripped[index]
            print('step 1')
#            result, index = decoder.raw_decode(buffer)
#            yield result
#            buffer = buffer[index:].lstrip()
        except ValueError:
          #not enough data to decode
          print("json_parse error")
          print('step 2')
          break
        
with open(data_read, 'r') as tsla_data:
#  for line in tsla_data:
    for chunk in json_parse(tsla_data):
#    for chunk in json_parse(tsla_data):
      #line_details = json.loads(data)[0]
#      print("testing ", i)
      print(chunk)
      print('step 3')


#try:
#  connection = mysql.connector.connect(host='127.0.0.1',
#                                       database='stonks_test_1',
#                                       user='test',
#                                       password='Testing123!')
                                       
#  with open(data_file3, 'r') as tsla_data:
#    for line in json_parse(tsla_data):
#      line_details = json.loads(line)[0]
#      #timestamp = line_details.get('ts', "NULL")
#      timestamp = str(int(time.time() * 1000))
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
      
#except mysql.connector.Error as error:
#  print("Failed to insert record into tsla_test_3 table {}".format(error))
      
#finally:
#  if (connection.is_connected()):
#    connection.close()
#    print("MySQL connection is closed")

