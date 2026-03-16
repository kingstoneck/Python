# py L:/Python/JSON_Read_Write_7_working.py

import sys
import time
import json
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

#def value_check(data, attribute, default_value):
#  return data.get(attribute) or NULL

#def json_check(data):
#  data_to = value_check(

line_details = []

with open('L:/aa_Stocks/Data/TSLA_05_26_20.txt', 'r') as tsla_data:
#with open('L:/aa_Stocks/Data/TSLA_Test_Data_JSON_1.txt', 'r') as tsla_data:
  for line in tsla_data:
    line_details = json.loads(line)[0]
    timestamp = str(int(time.time() * 1000))
    event = line_details.get('ev', "NULL")
    status = line_details.get('status', "NULL")
    message = line_details.get('message', "NULL")
    trade_symbol = line_details.get('sym', "NULL")
    trade_id = line_details.get('i', "NULL")
    exchange_id = line_details.get('x', "NULL")
    price = line_details.get('p', "NULL")
    volume = line_details.get('s', "NULL")
    condition = line_details.get('c', "NULL")
    trade_time = line_details.get('t', "NULL")
    tape = line_details.get('z', "NULL")
    try:
      connection = mysql.connector.connect(host='127.0.0.1',
                                           database='stonks_test_1',
                                           user='test',
                                           password='Testing123!')

      sql_insert = "INSERT INTO tsla_test_4 (ts, ev, status, msg, sym, i, x, p, s, c, t, z) " "VALUES (%s, %s, '%s', '%s', '%s', %s, %s, %s, %s, '%s', %s, %s)" % (timestamp, event, status, message, trade_symbol, trade_id, exchange_id, price, volume, condition, trade_time, tape)
      cursor = connection.cursor()
      cursor.execute(sql_insert)
      connection.commit()
      print("ts:",timestamp, ",",event, ",",status, ",",message, ",", trade_symbol, ",", trade_id, ",",
            exchange_id, ",", price, ",", volume, ",", condition, ",", trade_time, ",", tape)
      print(cursor.rowcount, "Record inserted successfully into tsla_test_2 table")
      cursor.close()
        
    except mysql.connector.Error as error:
      print("Failed to insert record into tsla_test_2 table {}".format(error))
      
    finally:
      if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")

