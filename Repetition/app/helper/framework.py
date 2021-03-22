# Helper .class method 

def class_name(instance):
    return instance.__class__.__name__

def str_to_bits(message):
    byte_array = bytearray(message, "utf8")
    byte_str = ""
    for byte in byte_array:
        binary_representation = bin(byte)[2:]
        if len(binary_representation) <= 7:
            binary_representation = '0' + binary_representation 

        byte_str += binary_representation
    return byte_str

def bits_to_str(message):
    string_message = ""
    for i in range(0, len(message), 7):
        block = message[i:i+7]
        ascii_value = int(block, 2)
        string_message += chr(ascii_value)
    return string_message    

def strbit2int(bit):
    return ord(bit) - ord('0')

def is_binary_message(message):
    counter = 0
    for i in message:
        counter += 1 if i not in ['0', '1'] else 0
    if counter > 0:
        return False
    return True

def save(file_name, content):
    f = open(file_name, 'w')
    f.write(content)
    f.close()
    return
  
def open_file(file_name):
    f = open(file_name, 'r')
    content = f.read()
    f.close()
    return content
