from helper.framework import strbit2int

# 
# For each N bits, find the most frequent occurrence
# 
def decode_message(received_message):
  message = ""
  for i in range(0, len(received_message), 3):
    block = received_message[i:i+3]
    counter = 0
    for j in range(len(block)):
      counter += strbit2int(block[j])
    message += '1' if counter>=2 else '0' 
    
  return message
