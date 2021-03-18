
def evaluate_bits(message, guess):
  if len(message)!=len(guess):
    return "The number of bits are not the same"
  counter = 0
  for i in range(len(message)):
    counter += 1 if message[i]==guess[i] else 0
  
  return (counter*100/len(message))

def average(samples, total):
  return samples/total