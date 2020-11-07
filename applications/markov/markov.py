import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
words = words.split()
words_dataset = {}
for i in range(len(words) - 1):
    if words[i] not in words_dataset:
        words_dataset[words[i]] = [words[i + 1]]
    else:
        words_dataset[words[i]].append(words[i + 1])

# TODO: construct 5 random sentences
keys = list(words_dataset.keys())

start_word = random.choice(keys)
while (len(start_word) < 2) or \
    not start_word[0].isupper() and \
    not (start_word[0] == '"' and start_word[1].isupper()):
    start_word = random.choice(keys)
print(start_word, end=' ')

stop_word = random.choice(keys)
while (len(stop_word) < 2) or \
    (stop_word[-1] not in ['.', '?', '!']) and \
    not ((stop_word[-2] in ['.', '?', '!']) and stop_word[-1] == '"'):
    print(stop_word, end=' ')
    stop_word = random.choice(keys)
print(stop_word)
