# py L:/Python/JSON_Read_Write_8_2.py

import sys
import time
import json
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

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

line_details = []
data_file1 = 'L:/aa_Stocks/Data/TSLA_05_26_20.txt'
data_file2 = 'L:/aa_Stocks/Data/TSLA_Test_Data_JSON_1.txt'
data_file3 = 'L:/aa_Stocks/Data/TSLA_Test_Data_JSON_2.txt'
data_file4 = 'L:/aa_Stocks/Data/Test_3_TSLA/TSLA_07_13_20_LE_format.txt'
data_file5 = 'C:/py/TSLA_07_13_20_LE_format2.txt'
data_file6 = 'L:/aa_Stocks/Data/TSLA_Test_Data_JSON_5.txt'

#cursor = connection.cursor()
#print("MySQL connection is open")

try:
  connection = mysql.connector.connect(host='127.0.0.1',
                                       database='stonks_test_2',
                                       user='test',
                                       password='Testing123!')                                 

  #with open(data_file1, 'r') as tsla_data:
  #    for line in tsla_data:
  #      line_details = json.loads(line)[0]

  with open(data_file6, 'r') as message:

  
    for line in message:
      line_details = json.loads(line)[0]
      svr_time = str(int(time.time() * 1000))
      event = line_details.get('ev', "NULL")
    
      if event == 'status':        
        status = line_details.get('status', "NULL")
        message = line_details.get('message', "NULL")
        sql_insert_i = "INSERT INTO test_i (ts, ev, status, msg) " "VALUES (%s, '%s', '%s', '%s')" % (svr_time, event, status, message)
        cursor = connection.cursor()
        cursor.execute(sql_insert_i)
        print("svr_ts:", svr_time, ", ev:", event, ", status:", status, ", message:", message, "\n",
              cursor.rowcount," Record inserted successfully into table: test_i.")
        connection.commit()
        
      elif event == 'T':
        trade_sym = line_details.get('sym', "NULL")
        exchange_id = line_details.get('x', "NULL")
        trade_id = line_details.get('i', "NULL")
        tape = line_details.get('z', "NULL")
        price = line_details.get('p', "NULL")
        volume = line_details.get('s', "NULL")
        condition = line_details.get('c', "NULL")
        trade_time = line_details.get('t', "NULL")

        print("svr_ts:", svr_time, ",", event, ",", trade_sym, ",", exchange_id, ",", trade_id, ",", tape, ",", price, ",", volume, 
              ",", condition, ",", trade_time, "\n", cursor.rowcount, " Record inserted successfully into table: tsla_test_t1.") 

        if trade_sym == 'TSLA':
          sql_insert_tsla_t = "INSERT INTO tsla_test_t1 (ts, ev, sym, x, i, z, p, s, c, t) " "VALUES (%s, '%s', '%s', %s, %s, %s, %s, %s, '%s', %s)" % (svr_time, event, trade_sym, exchange_id, trade_id, tape, price, volume, condition, trade_time)
          cursor = connection.cursor()
          cursor.execute(sql_insert_tsla_t)
          print("svr_ts:", svr_time, ",", event, ",", trade_sym, ",", exchange_id, ",", trade_id, ",", tape, ",", price, ",", volume, 
                ",", condition, ",", trade_time, "\n", cursor.rowcount, " Record inserted successfully into table: tsla_test_t1.")        
          connection.commit()
        elif trade_sym == 'AMAZ':
          sql_insert_amaz_t = "INSERT INTO amaz_test_t1 (ts, ev, sym, x, i, z, p, s, c, t) " "VALUES (%s, '%s', '%s', %s, %s, %s, %s, %s, '%s', %s)" % (svr_time, event, trade_sym, exchange_id, trade_id, tape, price, volume, condition, trade_time)
          cursor = connection.cursor()
          cursor.execute(sql_insert_amaz_t)
          print("svr_ts:", svr_time, ",", event, ",", trade_sym, ",", exchange_id, ",", trade_id, ",", tape, ",", price, ",", volume, 
                ",", condition, ",", trade_time, "\n", cursor.rowcount, " Record inserted successfully into table: amaz_test_t1.")         
          connection.commit()          
        else:
          print("Symbol " + trade_sym + " is not configured in Database...")
        
      elif event == 'A':
        trade_sym = line_details.get('sym', "NULL")
        tick_vol = line_details.get('s', "NULL")
        acc_vol = line_details.get('s', "NULL")
        day_open = line_details.get('op', "NULL")
        vwap = line_details.get('vw', "NULL")
        tick_open = line_details.get('p', "NULL")
        tick_close = line_details.get('p', "NULL")
        tick_high = line_details.get('p', "NULL")
        tick_low = line_details.get('p', "NULL")
        tick_avg = line_details.get('p', "NULL")
        tick_ts_start = line_details.get('t', "NULL")
        tick_ts_end = line_details.get('t', "NULL")
        
        if trade_sym == 'TSLA':
          sql_insert_tsla_a = "INSERT INTO tsla_test_a1 (ts, ev, sym, v, av, op, vw, o, c, h, l, a, s, e) " "VALUES (%s, '%s', '%s', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % (svr_time, event, trade_sym, tick_vol, acc_vol, day_open, vwap, tick_open, tick_close, tick_high, tick_low, tick_avg, tick_ts_start, tick_ts_end)        
          cursor = connection.cursor()
          cursor.execute(sql_insert_tsla_a)
          print("svr_ts:", svr_time, ",", event, ",", trade_sym, ",", tick_vol, ",", acc_vol, ",", day_open, ",", vwap, ",",
                tick_open, ",", tick_close, ",", tick_high, ",", tick_low, ",", tick_avg, ",", tick_ts_start, ",", tick_ts_end, "\n",
                cursor.rowcount, " Record inserted successfully into table: tsla_test_a1.")        
          connection.commit()
        elif trade_sym == 'AMAZ':
          sql_insert_amaz_a = "INSERT INTO amaz_test_a1 (ts, ev, sym, v, av, op, vw, o, c, h, l, a, s, e) " "VALUES (%s, '%s', '%s', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % (svr_time, event, trade_sym, tick_vol, acc_vol, day_open, vwap, tick_open, tick_close, tick_high, tick_low, tick_avg, tick_ts_start, tick_ts_end)        
          cursor = connection.cursor()
          cursor.execute(sql_insert_amaz_a)
          print("svr_ts:", svr_time, ",", event, ",", trade_sym, ",", tick_vol, ",", acc_vol, ",", day_open, ",", vwap, ",",
                tick_open, ",", tick_close, ",", tick_high, ",", tick_low, ",", tick_avg, ",", tick_ts_start, ",", tick_ts_end, "\n",
                cursor.rowcount, " Record inserted successfully into table: amaz_test_a1.")           
          connection.commit()
        else:
          print("Symbol " + trade_sym + " is not configured in Database...")

      elif event == 'AM':
        trade_sym = line_details.get('sym', "NULL")
        tick_vol = line_details.get('s', "NULL")
        acc_vol = line_details.get('s', "NULL")
        day_open = line_details.get('op', "NULL")
        vwap = line_details.get('vw', "NULL")
        tick_open = line_details.get('p', "NULL")
        tick_close = line_details.get('p', "NULL")
        tick_high = line_details.get('p', "NULL")
        tick_low = line_details.get('p', "NULL")
        tick_avg = line_details.get('p', "NULL")
        tick_ts_start = line_details.get('t', "NULL")
        tick_ts_end = line_details.get('t', "NULL")
        
        if trade_sym == 'TSLA':
          sql_insert_tsla_am = "INSERT INTO tsla_test_am1 (ts, ev, sym, v, av, op, vw, o, c, h, l, a, s, e) " "VALUES (%s, '%s', '%s', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % (svr_time, event, trade_sym, tick_vol, acc_vol, day_open, vwap, tick_open, tick_close, tick_high, tick_low, tick_avg, tick_ts_start, tick_ts_end)        
          cursor = connection.cursor()
          cursor.execute(sql_insert_tsla_am)
          print("svr_ts:", svr_time, ",", event, ",", trade_sym, ",", tick_vol, ",", acc_vol, ",", day_open, ",", vwap, ",",
                tick_open, ",", tick_close, ",", tick_high, ",", tick_low, ",", tick_avg, ",", tick_ts_start, ",", tick_ts_end, "\n",
                cursor.rowcount, " Record inserted successfully into table: tsla_test_am1.")         
          connection.commit()
        elif trade_sym == 'AMAZ':
          sql_insert_amaz_am = "INSERT INTO amaz_test_am1 (ts, ev, sym, v, av, op, vw, o, c, h, l, a, s, e) " "VALUES (%s, '%s', '%s', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % (svr_time, event, trade_sym, tick_vol, acc_vol, day_open, vwap, tick_open, tick_close, tick_high, tick_low, tick_avg, tick_ts_start, tick_ts_end)        
          cursor = connection.cursor()
          cursor.execute(sql_insert_amaz_am)
          print("svr_ts:", svr_time, ",", event, ",", trade_sym, ",", tick_vol, ",", acc_vol, ",", day_open, ",", vwap, ",",
                tick_open, ",", tick_close, ",", tick_high, ",", tick_low, ",", tick_avg, ",", tick_ts_start, ",", tick_ts_end, "\n",
                cursor.rowcount, " Record inserted successfully into table: amaz_test_am1.")           
          connection.commit()
        else:
          print("Symbol " + trade_sym + " is not configured in Database...")        
       
        
      elif event == 'Q':
        trade_sym = line_details.get('sym', "NULL")
        bid_exchange_id = line_details.get('bx', "NULL")
        bid_price = line_details.get('bp', "NULL")
        bid_size = line_details.get('bs', "NULL")
        ask_exchange_id = line_details.get('ax', "NULL")
        ask_price = line_details.get('ap', "NULL")
        ask_size = line_details.get('as', "NULL")
        condition = line_details.get('c', "NULL")
        trade_time = line_details.get('t', "NULL")
        
        if trade_sym == 'TSLA':
          sql_insert_tsla_q = "INSERT INTO tsla_test_q1 (ts, ev, sym, bx, bp, bs, ax, ap, as, c, t) " "VALUES (%s, '%s', '%s', %s, %s, %s, %s, %s, %s, '%s', %s)" % (svr_time, event, trade_sym, bid_exchange_id, bid_price, bid_size, ask_exchange_id, ask_price, ask_size, condition, trade_time)
          cursor = connection.cursor()
          cursor.execute(sql_insert_tsla_am)
          print("svr_ts:", svr_time, ",", event, ",", trade_sym, ",", bid_exchange_id, ",", bid_price, ",", bid_size, ",", 
                ask_exchange_id, ",", ask_price, ",", ask_size, ",", condition, ",", trade_time, "\n",
                cursor.rowcount," Record inserted successfully into table: tsla_test_q1.")
          connection.commit()
        elif trade_sym == 'AMAZ':
          sql_insert_amaz_q = "INSERT INTO amaz_test__q1 (ts, ev, sym, bx, bp, bs, ax, ap, as, c, t) " "VALUES (%s, '%s', '%s', %s, %s, %s, %s, %s, %s, '%s', %s)" % (svr_time, event, trade_sym, bid_exchange_id, bid_price, bid_size, ask_exchange_id, ask_price, ask_size, condition, trade_time)
          cursor = connection.cursor()
          cursor.execute(sql_insert_amaz_am)
          print("svr_ts:", svr_time, ",", event, ",", trade_sym, ",", bid_exchange_id, ",", bid_price, ",", bid_size, ",", 
                ask_exchange_id, ",", ask_price, ",", ask_size, ",", condition, ",", trade_time, "\n",
                cursor.rowcount," Record inserted successfully into table: amaz_test_q1.")       
          connection.commit()
        else:
          print("Symbol " + trade_sym + " is not configured in Database...")         
        
      elif event == 'NULL':
        print("No event read from WebSockets...")
        
      else:
        print("Error with event, no parameters loaded...")  
  
  
  
  
  
  
  #cursor = connection.cursor()  
  #with open(data_file1, 'r') as tsla_data:
  #    for line in tsla_data:
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
  #      sql_insert = "INSERT INTO tsla_test_4 (ts, ev, status, msg, sym, i, x, p, s, c, t, z) " "VALUES (%s, %s, '%s', '%s', '%s', %s, %s, %s, %s, '%s', %s, %s)" % (timestamp, event, status, message, trade_symbol, trade_id, exchange_id, price, volume, condition, trade_time, tape)
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
    #cursor.close()
    connection.close()
    print("MySQL connection is closed")

