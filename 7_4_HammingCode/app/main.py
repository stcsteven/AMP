from helper.framework import *
from helper.evaluator import *
from encoder import encode
from channel import *
from decoder import decode_message

# Main Function
def main():
    total_score = 0
    total_cases = 4
    for i in range(0, total_cases):
        file_name = "../datasets/input/"+ str(i) + ".txt"
        message = open_file(file_name)
        if not is_binary_message(message):
            message = str_to_bits(message) 
        # 
        # Main Algorithm
        # 
        coded_transmission = encode(message)
        
        received_message =  corrupt_message(coded_transmission)
        channel_file_name = "../datasets/channel/"+ str(i) + ".txt"
        save(channel_file_name, received_message)
        
        decoded_message = decode_message(received_message)
        output_file_name = "../datasets/output/"+ str(i) + ".txt"
        save(output_file_name, decoded_message)
        
        # Evaluate the Approach
        score = evaluate_bits(message, decoded_message)
        print("Message: "+ str(i) + " => Accuracy: "+ str(score) + "%")
        total_score += score
    
    print("Average Accuracy: "+ str(average(total_score, total_cases))+"%" )

if __name__ == "__main__":
    main()
