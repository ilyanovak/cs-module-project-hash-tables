def no_dups(s):
    s = s.split()
    processed = set()
    unique_words = [word for word in s if not (
        word in processed or processed.add(word))]
    unique_words = " ".join(unique_words)
    return unique_words


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
