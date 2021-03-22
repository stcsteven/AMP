from helper.framework import *

# 
# Repeat every bits N=3 times
# 
def encode(message):
  encoded_bit_list = ""
  for bit in message:
    encoded_bit_list += ( bit * 3 )
  return encoded_bit_list