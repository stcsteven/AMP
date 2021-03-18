from app.helper.framework import *
from app.encoder import encode
from app.channel import *
from app.decoder import decode_message

# Main Function
def main():
    message = open_file("datasets/input/1.txt")
    clean_message, coded_transmission = encode(message)
    print(clean_message)
    print(len(clean_message))
    received_message =  corrupt_message(coded_transmission)
    decoded_message = decode_message(received_message)
    print(decoded_message)
    print(len(decoded_message))
    print(message)
    print(bits_to_str(decoded_message))
    
if __name__ == "__main__":
    main()
