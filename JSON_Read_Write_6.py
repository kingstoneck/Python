# py L:/Python/JSON_Read_Write_6.py

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

with open('L:/aa_Stocks/Data/TSLA_Test_Data_JSON_1.json', 'r') as tsla_data:
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
      #mySql_insert_query = """INSERT INTO tsla_test_2
      #  SET ts = %s,
      #  """
      #mySql_insert_query = """INSERT INTO tsla_test_2 (ts, ev, status, msg, sym, i, x, p, s, c, t, z)
      #                        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""" % timestamp, event, status, message, symbol, trade_id, exchange_id, price, volume, condition, trade_time, tape
      #
      sql_insert = "INSERT INTO tsla_test_2 (ts, ev, status, msg, sym, i, x, p, s, c, t, z) " "VALUES (%s, %s, '%s', '%s', '%s', %s, %s, %s, %s, '%s', %s, %s)" % (timestamp, event, status, message, trade_symbol, trade_id, exchange_id, price, volume, condition, trade_time, tape)
      cursor = connection.cursor()
      #cursor.execute(
      #               "INSERT INTO tsla_test_2 (ts, ev)"
      #               "VALUES (%s, %s)",
      #               (timestamp, event)
      #cursor.execute(mySql_insert_query)
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

#with open('L:/aa_Stocks/Data/TSLA_Test_Data_JSON_2.txt', 'r') as tsla_data:
#  for line in tsla_data:
#    line_details.append(json.loads(line))
#    #["ev":None, "sym":None, "i":None, "x":None, "p":None, "s":None, "c":None, "t":None, "z":None]:
#      print("testing")
#      #timestamp = str(int(time.time() * 1000))
#      event = line_details['ev']
#      #status = line_details['status']
#      #message = line_details['message']
#      symbol = line_details['sym']
#      trade_id = line_details['i']
#      exchange_id = line_details['x']
#      price = line_details['p']
#      volume = line_details['s']
#      condition = line_details['c']
#      trade_time = line_details['t']
#      tape = line_details['z']
#      json_file.append(json.loads(line))
#      try:
#          connection = mysql.connector.connect(host='127.0.0.1',
#                                                 database='stonks_test_1',
#                                                 user='test',
#                                               password='Testing123!')
#          #####this part is not working####
#          mySql_insert_query = """INSERT INTO tsla_test_2(ev, sym, x, i, z, p, s, c, t)
#                                  VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
#                                  %(event, symbol, exchange_id, price, volume, condition, trade_time, tape)
#                                
#        ############
#        #removed status and msg from insert command
#
#          cursor = connection.cursor()
#          cursor.execute(mySql_insert_query)
#          connection.commit()
#          print(cursor.rowcount, "Record inserted successfully into tsla_test_1 table")
#          cursor.close()    
#        
#    except mysql.connector.Error as error:
#      print("Failed to insert record into tsla_test_1 table {}".format(error))
#
#    finally:
#      if (connection.is_connected()):
#          connection.close()
#          print("MySQL connection is closed")
#
#    print(line)
