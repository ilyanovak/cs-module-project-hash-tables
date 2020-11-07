# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

from collections import Counter

with open("ciphertext.txt") as f:
    old_codes = f.read()

codes_freq_tuples = Counter(char for char in old_codes if char.isalpha()).most_common()
# print(freq_tuple)

codes_freq_list = []
for freq in codes_freq_tuples:
    codes_freq_list.append(freq[0])
# print(codes_freq_list)

actual_freq_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W',
               'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

new_codes = ""
for char in old_codes:
    if char.isspace() or char == 'â':
        new_codes += char
    elif char in codes_freq_list:
        index = codes_freq_list.index(char)
        new_codes += actual_freq_list[index]

print(new_codes)
