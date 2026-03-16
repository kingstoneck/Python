# py L:/Python/WS_Read_Write_1.py

import sys
import time
import json
import websocket
import functools
import configparser
import mysql.connector
from json import JSONDecoder
from functools import partial
from mysql.connector import Error
from mysql.connector import errorcode

#
#Need to read multiple objects in 1 line of json
#Need to nest define functions for connection
#Need to enable a reconnect loop if the mysql connection drops
#Need to write to error file if the mysql connection fails so we do not lose data
#

cfg = configparser.ConfigParser()
cfg.read('L:/aa_Stocks/Production/conf/stonkconfig.ini')
usr = 'user2'

data_details = []
line_details = []

#data_file_use = data_file2
#data_parse = data_file_use
#data_read = data_file_use

#def json_parse(fileobj, decoder=JSONDecoder(), buffersize=1024000):
#  buffer = ''
#  with open(message, 'r') as file_obj:
#    for chunk in iter(functools.partial(file_obj.read, buffersize), ''):
#      buffer += chunk
#      while buffer:
#        try:
#            result, index = decoder.raw_decode(buffer)
#            yield result
#            buffer = buffer[index:].lstrip()
#        except ValueError:
#            #not enough data to decode
#            print("json_parse error")
#            break

def on_message(ws, message):
  with (cfg[usr]['data_file'], 'a') as sd:
    #sd = streaming data
    for line in message:
      line_details = json.loads(line)[0]
      svr_time = str(int(time.time() * 1000))
      timestamp = line_details.get('ts', "NULL")
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
        
      sql_insert = "INSERT INTO tsla_test_4 (ts, ev, status, msg, sym, i, x, p, s, c, t, z) " "VALUES (%s, %s, '%s', '%s', '%s', %s, %s, %s, %s, '%s', %s, %s)" % (timestamp, event, status, message, trade_symbol, trade_id, exchange_id, price, volume, condition, trade_time, tape)
      cursor = connection.cursor()
      cursor.execute(sql_insert)
      connection.commit()
      
      print("svr_ts:",svr_time, ",ts:",timestamp, ",",event, ",",status, ",",message, ",", trade_symbol, ",", trade_id, 
            ",", exchange_id, ",", price, ",", volume, ",", condition, ",", trade_time, ",", tape, cursor.rowcount, 
            "\n Record inserted successfully into tsla_test_3 table") 
      cursor.close()

  
def on_error(ws, error):
  with open(cfg[usr]['log_file'], 'a') as sde:
    #sde = streaming data error, this is the log file
    #sde.write(error + "\n")
    for line in error:
      line_details = json.loads(error)[0]
      svr_time = str(int(time.time() * 1000))
      timestamp = line_details.get('ts', "NULL")
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
        
      sql_insert = "INSERT INTO tsla_test_4 (ts, ev, status, msg, sym, i, x, p, s, c, t, z) " "VALUES (%s, %s, '%s', '%s', '%s', %s, %s, %s, %s, '%s', %s, %s)" % (timestamp, event, status, message, trade_symbol, trade_id, exchange_id, price, volume, condition, trade_time, tape)
      cursor = connection.cursor()
      cursor.execute(sql_insert)
      connection.commit()
      
      sde.write(error + "\n")
      print("svr_ts:",svr_time, ",ts:",timestamp, ",",event, ",",status, ",",message, ",", trade_symbol, ",", trade_id, 
            ",", exchange_id, ",", price, ",", volume, ",", condition, ",", trade_time, ",", tape, cursor.rowcount, 
            "\n Record inserted successfully into tsla_test_3 table") 
      cursor.close()    
    #sd.write("\n")
    #print(error)
  
def on_close(ws):
  with open("L:/aa_Stocks/Data/Test_3_TSLA/test_1.txt", 'a') as sd:
    sd.write("Websocket Is Now Closed" + "\n")
    #sd.write("\n")
    print("Websocket Is Now Closed")

def on_open(ws):
  ws.send('{"action":"auth","params":"AKI0MR6OJF4F93Q7Y89H"}')
  ws.send('{"action":"subscribe","params":"T.TSLA"}')
  

while True:
  if __name__ == "__main__":
    try:
      connection = mysql.connector.connect(host='127.0.0.1',
                                           database='stonks_test_1',
                                           user='test',
                                           password='Testing123!')
      print("MySQL is connected, connecting to WS.")

      try:      
        # websocket.enableTrace(True)
        ws = websocket.WebSocketApp("wss://alpaca.socket.polygon.io/stocks",
          on_message = on_message,
          on_error = on_error,
          on_close = on_close)
        ws.on_open = on_open
        ws.run_forever()
        with open("L:/aa_Stocks/Data/Test_3_TSLA/test_1.txt", 'a') as sd:
          sd.write("Websocket Is Reconnecting" + "\n")
          #sd.write("\n")
          print("Websocket Is Reconnecting")
      except:
        pass
        
    except mysql.connector.Error as error:
      print("MySQL is not connected. \n")
      print("Failed to insert record into tsla_test_4 table {}".format(error))
      
    finally:
      if (connection.is_connected()):
        #cursor.close()
        connection.close()
        print("MySQL connection is closed") 

ws.close() 

