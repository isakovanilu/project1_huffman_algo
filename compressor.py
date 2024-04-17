from collections import Counter


def read_input(input_file):
    with open(input_file,'r') as file:
        input_data = file.read()
        # splitting the data into separate lines
        # using the split() function
        lines = input_data.split()
        
        # create a counter object to count occurrences of each word
        word_count = Counter(lines)
    
        # convert the counter object to a dictionary
        word_count_dict = dict(word_count)
        print(word_count_dict)
        return word_count_dict
read_input('input.txt')