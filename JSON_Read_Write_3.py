# py L:/Python/JSON_Read_Write_3.py

import sys
import time
import json

#import mysql.connector
#from mysql.connector import Error
#from mysql.connector import errorcode

line_details = []
#i=1

with open('L:/aa_Stocks/Data/TSLA_Test_Data_JSON_1.json', 'r') as tsla_data:
  for line in tsla_data:
    line_details = json.loads(line)[0]
#    line_details.append(json.loads(line))[0] - object not subscriptable
#    we should not need to append the line_details table, as we will write the number for each line
#    line_details.append(json.loads(line))
    timestamp = str(int(time.time() * 1000))
    event = line_details['ev']
    #status = line_details['status']
    #message = line_details['message']
    symbol = line_details['sym']
    trade_id = line_details['i']
    exchange_id = line_details['x']
    price = line_details['p']
    volume = line_details['s']
    #condition = line_details['c']
    trade_time = line_details['t']
    tape = line_details['z']
    print("ts:", timestamp, ",", event, ",", symbol, ",", trade_id, ",", exchange_id, ",", price, ",", volume, ",", trade_time, ",", tape)



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
