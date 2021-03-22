from helper.framework import strbit2int
import random

bad_bits_probability = 0.05

def generate_noise(length):
  return random.choices(population = ['0','1'], weights = [1-bad_bits_probability, bad_bits_probability], k=length)
  
def corrupt_message(message):
  new_message = ""
  noise = generate_noise(len(message))
  for i in range(len(message)):
    bit = str((strbit2int(message[i]) + strbit2int(noise[i]))%2)
    new_message += bit
  
  return new_message