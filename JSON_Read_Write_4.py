# py L:/Python/JSON_Read_Write_4.py

import sys
import time
import json

line_details = []
i=1

with open('L:/aa_Stocks/Data/TSLA_Test_Data_JSON_2.json', 'r') as tsla_data:
  for line in tsla_data:
    line_details.append(json.loads(line))
    print("testing ")
#	i=i+1