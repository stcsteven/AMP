from helper.framework import *
from helper.evaluator import *
from encoder import encode
from channel import *
from decoder import decode_message

# Main Function
def main():
    total_score = 0
    total_cases = 11
    for i in range(0, total_cases):
        file_name = "../datasets/input/"+ str(i) + ".txt"
        message = open_file(file_name)
        # 
        # Main Algorithm
        # 
        clean_message, coded_transmission = encode(message)
        received_message =  corrupt_message(coded_transmission)
        decoded_message = decode_message(received_message)
        
        score = evaluate_bits(clean_message, decoded_message)
        print("Message: "+ str(i) + " => Accuracy: "+ str(score) + "%")
        total_score += score
    
    print("Average Accuracy: "+ str(average(total_score, total_cases))+"%" )

if __name__ == "__main__":
    main()
