from collections import defaultdict


def is_unique_chars_v1(str):
    """
    Let N be the string length
    List construction: O(N)
    Set construction: O(N)
    len function: O(1)
    => O(N)
    """
    chars = list(str)
    unique_chars = set(chars)
    return len(chars) == len(unique_chars)


def is_unique_chars_v2(str):
    """
    Let N be the string length
    Dictionary construction: O(N); d[k] = v is O(1), done N times
    Containment check: O(N)
    => O(N)
    """
    chars_map = defaultdict(int)
    for char in str:
        chars_map[char] += 1
    return 2 not in chars_map.values()


if __name__ == '__main__':
    str = "Hello"
    print(is_unique_chars_v1(str))
    print(is_unique_chars_v2(str))
