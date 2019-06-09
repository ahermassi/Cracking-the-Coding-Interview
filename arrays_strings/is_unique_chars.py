def is_unique_chars_v1(str):
    """
    Let N be the string length
    List creation: O(N)
    Set creation: O(N)
    len function: O(1)
    => O(N)
    """
    chars = list(str)
    unique_chars = set(chars)
    return len(chars) == len(unique_chars)


if __name__ == '__main__':
    s = "Hello"
    print(is_unique_chars_v1(s))
