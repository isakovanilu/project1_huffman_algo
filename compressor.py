import heapq
from collections import Counter

def calculate_frequencies(input_file):
    with open(input_file,'r') as file:
        text = file.read() #.split()
    # freq = Counter(text)
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

print(calculate_frequencies('input.txt'))

def build_huffman_tree(frequencies):
    heap = [[freq, [sym, ""]] for sym, freq in frequencies.items()]
    print(heap)


frequencies = calculate_frequencies('input.txt')

print(build_huffman_tree(frequencies))