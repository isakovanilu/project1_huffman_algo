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


def build_huffman_tree(frequencies):
    heap = [[freq, [sym, ""]] for sym, freq in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def compress(input_file, codes):
    with open(input_file,'r') as file:
        text = file.read() #.split()
    return ''.join(code for char in text for sym, code in codes if char == sym)


def decompress(compressed_text, codes):
    reverse_codes = {code: sym for sym, code in codes}
    current_code = ""
    decompressed_text = ""
    for bit in compressed_text:
        current_code += bit
        if current_code in reverse_codes:
            decompressed_text += reverse_codes[current_code]
            current_code = ""
    return decompressed_text
    
    
    
input_file = 'input.txt'
# calculate frequencies and build Huffman tree
frequencies = calculate_frequencies(input_file)
huffman_tree = build_huffman_tree(frequencies)

# generate Huffman codes
codes = [(sym, code) for sym, code in huffman_tree]

# compress and decompress
compressed_text = compress(input_file, codes)
decompressed_text = decompress(compressed_text, codes)

print('decompressed_text', decompressed_text)