import heapq
import os

# function to calculate character frequencies in the input file
def calculate_frequencies(input_file):
    with open(input_file, 'r') as file:
        text = file.read()
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

# function to build the huffman tree and generate codes
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

# function to compress the input text using the huffman codes
def compress(input_file, codes, output_file):
    with open(input_file, 'r') as file:
        text = file.read()
    compressed_text = ''.join(code for char in text for sym, code in codes if char == sym)
    
    # writing compressed text to file
    with open(output_file, 'w') as file:
        file.write(compressed_text)

# function to decompress the compressed text using the huffman codes
def decompress(input_file, codes, output_file):
    reverse_codes = {code: sym for sym, code in codes}
    
    # read compressed text from file
    with open(input_file, 'r') as file:
        compressed_text = file.read()
    
    current_code = ""
    decompressed_text = ""
    for bit in compressed_text:
        current_code += bit
        if current_code in reverse_codes:
            decompressed_text += reverse_codes[current_code]
            current_code = ""
    
    # writing decompressed text to file
    with open(output_file, 'w') as file:
        file.write(decompressed_text)

# main process
input_file = 'shakespeare.txt'
compressed_file = 'compressed.txt'
decompressed_file = 'decompressed.txt'

# calculate frequencies and build huffman tree
frequencies = calculate_frequencies(input_file)
huffman_tree = build_huffman_tree(frequencies)

# generate huffman codes
codes = [(sym, code) for sym, code in huffman_tree]

# compress the input file and write to compressed file
compress(input_file, codes, compressed_file)

# decompress the compressed file and write to decompressed file
decompress(compressed_file, codes, decompressed_file)

# verify decompression
with open(input_file, 'r') as original, open(decompressed_file, 'r') as decompressed:
    assert original.read() == decompressed.read(), "decompression failed!"

print('compression and decompression successful. check the files for results.')
