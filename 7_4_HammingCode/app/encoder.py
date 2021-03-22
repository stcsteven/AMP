from helper.framework import *

# 
# Use 7.4 Hamming code encoder where
# t5 = s1+s2+s3
# t6 = s2+s3+s4
# t7 = s1+s3+s4
#
addition_rules = [[0, 1, 2], 
                  [1, 2, 3], 
                  [0, 2, 3]]

def addition_bits(message, vector_rule):
  return (strbit2int(message[vector_rule[0]])+ strbit2int(message[vector_rule[1]]) + strbit2int(message[vector_rule[2]]))%2

def encode(message):
  encoded_message = ""
  for i in range(0, len(message), 4):
    block_message = message[i:i+4]
    added_bits = ""
    for i in range(0, 3):
      added_bits += str(addition_bits(block_message, addition_rules[i]))  
    encoded_message += (block_message + added_bits)
  return encoded_message