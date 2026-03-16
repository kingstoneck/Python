# py L:/Python/JSON_Read_3.py

import json

json_file = []
with open('L:/aa_Stocks/Data/TSLA_Test_Data_JSON_4.txt', 'r') as tsla_data:
  for line in tsla_data:
    json_file.append(json.loads(line))
    print(line)



#
#example from https://pynative.com/python-mysql-insert-data-into-database-table/

#import mysql.connector
#from mysql.connector import Error
#from mysql.connector import errorcode
#
#try:
#    connection = mysql.connector.connect(host='127.0.0.1',
#                                         database='sql_test_1',
#                                         user='test',
#                                         password='Testing123!')
#    mySql_insert_query = """INSERT INTO test_table_1 (Id, Name, Price, Date) 
#                           VALUES 
#                           (11, 'Lenovo ThinkPad P71', 6459, '2019-08-14') """
#
#    cursor = connection.cursor()
#    cursor.execute(mySql_insert_query)
#    connection.commit()
#    print(cursor.rowcount, "Record inserted successfully into test_table_1 table")
#    cursor.close()
#
#except mysql.connector.Error as error:
#    print("Failed to insert record into test_table_1 table {}".format(error))
#
#finally:
#    if (connection.is_connected()):
#        connection.close()
#        print("MySQL connection is closed")
#
#