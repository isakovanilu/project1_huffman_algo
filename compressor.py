from collections import Counter

with open(r'input.txt','r') as file:
    input_data = file.read()
    # splitting the data into separate lines
    # using the split() function
    lines = input_data.split()
    print('lines', lines)
    
    # create a counter object to count occurrences of each word
    word_count = Counter(lines)

    # convert the counter object to a dictionary
    word_count_dict = dict(word_count)
    print(word_count_dict)