from app.helper.framework import *

# 
# Repeat every bits N=3 times
# 
def encode(message):
  bit_list = str_to_bits(message)
  encoded_bit_list = ""
  for bit in bit_list:
    encoded_bit_list += ( bit * 3 )
  return bit_list, encoded_bit_list