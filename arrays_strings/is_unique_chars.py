def is_unique_chars(s):
    chars = list(s)
    unique_chars = set(chars)
    return len(chars) == len(unique_chars)


if __name__ == '__main__':
    s = "Hello"
    print(is_unique_chars(s))
