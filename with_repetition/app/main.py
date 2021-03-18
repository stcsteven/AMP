from helper.framework import *
from encoder import encode
from channel import *
from decoder import decode_message

# Main Function
def main():
    message = open_file("../datasets/input/1.txt")
    clean_message, coded_transmission = encode(message)
    received_message =  corrupt_message(coded_transmission)
    decoded_message = decode_message(received_message)
    print(bits_to_str(decoded_message))

if __name__ == "__main__":
    main()
