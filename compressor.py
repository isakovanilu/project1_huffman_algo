
def calculate_frequencies(input_file):
    with open(input_file,'r') as file:
        text = file.read()
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

print(calculate_frequencies('input.txt'))