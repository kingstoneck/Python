# py L:/Python/JSON_Read_Write_14.py

#import sys
#import time
import json
#import functools
#import mysql.connector
#from json import JSONDecoder
#from functools import partial
#from mysql.connector import Error
#from mysql.connector import errorcode

#
#Need to read multiple objects in 1 line of json
#Need to nest define functions for connection
#Need to enable a reconnect loop if the mysql connection drops
#Need to write to error file if the mysql connection fails so we do not lose data
#

#data_details = []
data_file1 = 'L:/aa_Stocks/Data/TSLA_05_26_20.txt'
data_file2 = 'L:/aa_Stocks/Data/TSLA_Test_Data_JSON_1.txt'
data_file3 = 'L:/aa_Stocks/Data/TSLA_Test_Data_JSON_2.txt'
data_file4 = 'L:/aa_Stocks/Data/Test_3_TSLA/TSLA_07_13_20_LE_format.txt'
data_file5 = '''{"_index": "1234", "_type": "11", "_id": "1234", "_score": 0.0, "fields": {"c_u": ["url.com"], "tawgs.id": ["p6427"]}}{"_index": "1234", "_type": "11", "_id": "786fd4ad2415aa7b", "_score": 0.0, "fields": {"c_u": ["url2.com"], "tawgs.id": ["p12519"]}}{"_index": "1234", "_type": "11", "_id": "5826e7cbd92d951a", "_score": 0.0, "fields": {"tawgs.id": ["p8453", "p8458"]}}'''
data_file6 = '''{"ev":"T","sym":"TSLA","i":"40578","x":12,"p":819.44,"s":5,"c":[37],"t":1589913367558,"z":3}'''#,{"ev":"T","sym":"TSLA","i":"40579","x":12,"p":819.41,"s":17,"c":[37],"t":1589913367570,"z":3},{"ev":"T","sym":"TSLA","i":"31727","x":4,"p":819.4204,"s":17,"c":[37],"t":1589913367573,"z":3},{"ev":"T","sym":"TSLA","i":"12962","x":11,"p":819.4,"s":10,"c":[37],"t":1589913367576,"z":3},{"ev":"T","sym":"TSLA","i":"40580","x":12,"p":819.4,"s":1,"c":[37],"t":1589913367589,"z":3},{"ev":"T","sym":"TSLA","i":"8809","x":8,"p":819.4,"s":2,"c":[14,37,41],"t":1589913367589,"z":3}]'''

#       The function below works when there is 1 array, and breaks when the outer [] are deleted.  A single object with {} works fine.

data_file_use = data_file6
data_parse = data_file_use
data_read = data_file_use

d = json.JSONDecoder()

idx = 0

while True:
  if idx >= len(data_read):
    break
  data, i = d.raw_decode(data_read[idx:])
  idx += i
  print(data)
  print('*' * 80)

#
###             Below is not working correctly
#
#C:\Users\kings>py L:/Python/JSON_Read_Write_13.py
#MySQL connection is closed
#Traceback (most recent call last):
#  File "L:/Python/JSON_Read_Write_13.py", line 53, in <module>
#    data_details = json.loads(data)[0]
#  File "C:\Program Files\Python38\lib\json\__init__.py", line 341, in loads
#    raise TypeError(f'the JSON object must be str, bytes or bytearray, '
#TypeError: the JSON object must be str, bytes or bytearray, not list
#

#def json_parse(fileobj, decoder=JSONDecoder(), buffersize=1024000):
#  buffer = ''
#  with open(data_parse, 'r') as file_obj:
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
#        
#try:
#  connection = mysql.connector.connect(host='127.0.0.1',
#                                       database='stonks_test_1',
#                                       user='test',
#                                       password='Testing123!')   
#                                       
#  with open(data_read, 'r') as tsla_data:
#    for data in json_parse(tsla_data):
#        data_details = json.loads(data)[0]
#        #timestamp = data_details.get('ts', "NULL")
#        timestamp = str(int(time.time() * 1000))
#        event = data_details.get('ev', "NULL")
#        status = data_details.get('status', "NULL")
#        message = data_details.get('message', "NULL")
#        trade_symbol = data_details.get('sym', "NULL")
#        trade_id = data_details.get('i', "NULL")
#        exchange_id = data_details.get('x', "NULL")
#        price = data_details.get('p', "NULL")
#        volume = data_details.get('s', "NULL")
#        condition = data_details.get('c', "NULL")
#        trade_time = data_details.get('t', "NULL")
#        tape = data_details.get('z', "NULL")
#        
#        sql_insert = "INSERT INTO tsla_test_5 (ts, ev, status, msg, sym, i, x, p, s, c, t, z) " "VALUES (%s, %s, '%s', '%s', '%s', %s, %s, %s, %s, '%s', %s, %s)" % (timestamp, event, status, message, trade_symbol, trade_id, exchange_id, price, volume, condition, trade_time, tape)
#        cursor = connection.cursor()
#        cursor.execute(sql_insert)
#        connection.commit()
#        print("ts:",timestamp, ",",event, ",",status, ",",message, ",", trade_symbol, ",", trade_id, ",",
#              exchange_id, ",", price, ",", volume, ",", condition, ",", trade_time, ",", tape)
#        print(cursor.rowcount, "Record inserted successfully into tsla_test_4 table")
#        cursor.close()
#          
#except mysql.connector.Error as error:
#  print("Failed to insert record into tsla_test_4 table {}".format(error))
#      
#finally:
#  if (connection.is_connected()):
#    #cursor.close()
#    connection.close()
#    print("MySQL connection is closed")