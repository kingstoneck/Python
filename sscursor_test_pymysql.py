#  py L:\Python\sscursor_test_pymysql.py

import configparser

#import MySQLdb
#import MySQLdb.cursors
#from MySQLdb import _mysql
import pymysql
import pymysql.cursors
#import pymysql.cursors
#import mysql.connector

cfg = configparser.ConfigParser()
cfg.read('L:/aa_Stocks/Production/conf/stonkconfig.ini')

db_connection = pymysql.connect(host=cfg['mysql_test_2']['host'],
                                database=cfg['mysql_test_2']['db'],
                                user=cfg['mysql_test_2']['usr'],
                                password=cfg['mysql_test_2']['pwd'],
                                cursorclass=pymysql.cursors.SSCursor
                                )

connection_cursor = db_connection.cursor()

last_load_time = 0
first_time_flag = True

def pass_time(servertime):
  last_load_time = servertime
  return last_load_time

try:
  while True:
    if __name__ == "__main__":
      fetch_after_init = f"SELECT * FROM tsla_test_am1 WHERE servertime > '{last_load_time}'" # LIMIT 1"
      connection_cursor.execute(fetch_after_init)
      new_result = connection_cursor.fetchall()
      for data in new_result: 
        u_id = data[0]
        servertime = data[1]
        event = data[2]
        symbol = data[3]
        tickvolume = data[4]
        accumvolume = data[5]
        openprice = data[6]
        vwap = data[7]
        tickopen = data[8]
        tickclose = data[9]
        tickhigh = data[10]
        ticklow = data[11]
        tickavg = data[12]
        tickstart = data[13]
        tickend = data[14]
        last_load_time = pass_time(servertime)
        #print_info(u_id, servertime, event, symbol, tickvolume, accumvolume, openprice, vwap, tickopen, tickclose, tickhigh, ticklow, 
        #           tickavg, tickstart, tickend, trade_list, last_load_time
        #           )
        print(u_id, servertime, event, symbol, tickvolume, accumvolume, openprice, vwap, tickopen, tickclose, tickhigh, ticklow, 
                   tickavg, tickstart, tickend, last_load_time
                   )
      db_connection.commit()

except KeyboardInterrupt:
  print("\n" , " Process halted with Keyboard Interrupt!")





#      print("MySQL is connecting...")
#
#    print("MySQL is connected to", cfg['mysql_test_2']['db'],"!")





#db_connection = mysql.connector.connect(host=cfg['mysql_test_2']['host'],
#                                        database=cfg['mysql_test_2']['db'],
#                                        user=cfg['mysql_test_2']['usr'],
#                                        password=cfg['mysql_test_2']['pwd'],
#                                        cursorclass=MySQLdb.cursors.SSCursor
#                                         )
#

#
#db_connection = _mysql.connect(host=cfg['mysql_test_2']['host'],
#                                      db=cfg['mysql_test_2']['db'],
#                                      user=cfg['mysql_test_2']['usr'],
#                                      passwd=cfg['mysql_test_2']['pwd'],
#                                      cursorclass=MySQLdb.cursors.SSCursor
#                                      )
