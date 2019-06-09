from collections import defaultdict


def is_unique_chars_v1(str):
    """
    Let N be the string length
    List construction: O(N)
    Set construction: O(N)
    len function: O(1)
    => O(N) time
    => O(N) space
    """
    chars = list(str)
    unique_chars = set(chars)
    return len(chars) == len(unique_chars)


def is_unique_chars_v2(str):
    """
    Let N be the string length
    Dictionary construction: O(N); d[k] = v is O(1), done N times
    Containment check: O(N)
    => O(N) time
    => O(N) space
    """
    chars_map = defaultdict(int)
    for char in str:
        chars_map[char] += 1
    return 2 not in chars_map.values()


def is_unique_chars_v3(str):
    """
    If not allowed to use additional data structures, we can compare every character of the string to every other
    character of the string.
    This will take 0(n ** 2) time and 0(1) space
    """
    for char1 in str:
        occurrence = 0
        for char2 in str:
            if char1 == char2:
                occurrence += 1
            if occurrence > 1:
                return False
    return True


if __name__ == '__main__':
    str = "Hello"
    print(is_unique_chars_v1(str))
    print(is_unique_chars_v2(str))
    print(is_unique_chars_v3(str))
