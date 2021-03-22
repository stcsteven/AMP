from helper.framework import strbit2int

# Use 7.4 Hamming code encoder where
# r5 = r1+r2+r3
# r6 = r2+r3+r4
# r7 = r1+r3+r4
#
guess_flip = [2, 1, 0, -1, 3, -1, -1, -1]
addition_rules = [[0, 1, 2], 
                  [1, 2, 3], 
                  [0, 2, 3]]

def addition_bits(message, vector_rule):
  return (strbit2int(message[vector_rule[0]])+ strbit2int(message[vector_rule[1]]) + strbit2int(message[vector_rule[2]]))%2

def flip(message, idx):
  message = list(message)
  if message[idx] == '0':
    message[idx] = '1'  
  elif message[idx] == '1':
    message[idx] = '0'
  return ''.join(message)

def decode_message(received_message):
  message = ""
  for i in range(0, len(received_message), 7):
    assumed_message = received_message[i:i+4]
    parity_bits = received_message[i+4:i+7]
    counter = 0
    for i in range(len(parity_bits)):
      counter |= 1 if str(addition_bits(assumed_message, addition_rules[i])) == parity_bits[i] else 0
      if i < len(parity_bits)-1:
        counter <<=1 
    if guess_flip[counter] > 0:
      assumed_message = flip(assumed_message, guess_flip[counter])
    message+=assumed_message
  return message
