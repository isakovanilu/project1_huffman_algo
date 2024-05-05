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
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        print(lo)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

frequencies = calculate_frequencies('input.txt')

print(build_huffman_tree(frequencies))