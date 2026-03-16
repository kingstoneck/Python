# py L:\Python\maths\macd_test_calc.py

import decimal
from collections import deque

#changing from a deque to a value
#macd1_d = decimal.Decimal('670.1785') #(deque([decimal.Decimal('0')] * 2))
#macd1_d = deque([decimal.Decimal('0'), decimal.Decimal('0')])
#macd2_d = deque([0] * 2)
#macd3_d = deque([0] * 2)

macd1 = decimal.Decimal('0')
macd2 = decimal.Decimal('0')
macd3 = decimal.Decimal('0')

macd1_calc = decimal.Decimal('0')
macd2_calc = decimal.Decimal('0')
macd3_calc = decimal.Decimal('0')


macd1_var = decimal.Decimal(input("macd1 = "))
macd2_var = decimal.Decimal(input("macd2 = "))
macd3_var = decimal.Decimal(input("macd3 = "))
macd_offset = decimal.Decimal(input("macd offset = "))
macd_smooth = decimal.Decimal(input("macd smoothing = "))
#macd1_var = input("macd1 = ")
trade_list = deque([decimal.Decimal('606.0141'), decimal.Decimal('606.0143'), decimal.Decimal('606.0145'), decimal.Decimal('606.0152'), decimal.Decimal('606.0162'), decimal.Decimal('606.0179'), decimal.Decimal('606.0182'), decimal.Decimal('606.0189'), decimal.Decimal('606.0205'), decimal.Decimal('606.0226'), decimal.Decimal('606.0224'), decimal.Decimal('606.0224'), decimal.Decimal('606.0225'), decimal.Decimal('606.0226'), decimal.Decimal('606.0226'), decimal.Decimal('606.0229'), decimal.Decimal('606.0231'), decimal.Decimal('606.0236'), decimal.Decimal('606.0287'), decimal.Decimal('606.0297'), decimal.Decimal('606.0312'), decimal.Decimal('606.0322'), decimal.Decimal('606.0333'), decimal.Decimal('606.0337'), decimal.Decimal('606.0344'), decimal.Decimal('606.0355'), decimal.Decimal('606.0368'), decimal.Decimal('606.0377'), decimal.Decimal('606.0396'), decimal.Decimal('606.0410'), decimal.Decimal('606.0424'), decimal.Decimal('606.0443'), decimal.Decimal('606.0475'), decimal.Decimal('606.0481'), decimal.Decimal('606.0491'), decimal.Decimal('606.0496'), decimal.Decimal('606.0523'), decimal.Decimal('606.0536'), decimal.Decimal('606.0550'), decimal.Decimal('606.0556'), decimal.Decimal('606.0573'), decimal.Decimal('606.0586'), decimal.Decimal('606.0595'), decimal.Decimal('606.0614'), decimal.Decimal('606.0628'), decimal.Decimal('606.0641'), decimal.Decimal('606.0652'), decimal.Decimal('606.0659'), decimal.Decimal('606.0667'), decimal.Decimal('606.0694')])
trade_list_test = decimal.Decimal('606.0141')

#print(trade_list)
#print(decimal.Decimal(trade_list[0]))
#print(macd1_var, macd_smooth)

def calc_macd(macd1, macd2, macd3, macd1_var, macd2_var, macd3_var, macd_offset, macd_smooth, trade_list):
  macd1_calc = (trade_list[0] * (macd_smooth / (1 + macd1_var))) + (macd1 * (1 - (macd_smooth / (1 + macd1_var))))
  macd2_calc = (trade_list[0] * (macd_smooth / (1 + macd2_var))) + (macd2 * (1 - (macd_smooth / (1 + macd2_var))))
  macd3_calc = (trade_list[0] * (macd_smooth / (1 + macd3_var))) + (macd3 * (1 - (macd_smooth / (1 + macd3_var))))
  macd1 = macd1_calc
  macd2 = macd2_calc
  macd3 = macd3_calc
  print("MACD = ", macd1, macd2, macd3)
  return macd1, macd2, macd3

calc_macd(macd1, macd2, macd3, macd1_var, macd2_var, macd3_var, macd_offset, macd_smooth, trade_list)