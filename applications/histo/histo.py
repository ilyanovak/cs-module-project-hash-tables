from collections import Counter

with open("robin.txt") as f:
    words = f.read()

words = words.lower()

char_list = ['"', ':', ',', '.', '-', '+', '=', '/',
             '\\', ' | ', '[', '] ', '{', '} ', '(', ') ', '* ' ' ^ ' ' & ']
for char in char_list:
    words = words.replace(char, "")

words = words.split()

frequencies = Counter(words).most_common(25)

frequencies_temp = frequencies
frequencies_temp.sort(key=lambda x: len(x[0]), reverse=True)
longest_word_length = len(frequencies_temp[0][0])

frequencies.sort(key=lambda x: x[1], reverse=True)

for word in frequencies:
    print(word[0] + ' ' * (longest_word_length -
                           len(word[0]) + 5) + '#' * word[1])
