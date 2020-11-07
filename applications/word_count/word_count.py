from collections import Counter


def word_count(s):
    s = s.lower()
    char_list = ['"', ':', ';', ',', '.', '-', '+', '=', '/',
                 '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    for char in char_list:
        s = s.replace(char, "")
    words = s.split()
    words = dict(Counter(words))
    if '' in words:
        words.pop('')
    return words



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
