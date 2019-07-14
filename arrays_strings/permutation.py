"""
Given two strings, write a method to decide if one is a permutation of the
other.
"""
from collections import defaultdict


def permutation1(str1, str2):
    """
    sorted function: Timsort, O(N log N)
    Strings comparison: O(N)
    => O(N log N) time
    => O(N) space
    """
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)  # sort() method works only with lists; list(str1).sort(), returns None


def permutation2(str1, str2):
    """
    Dictionary construction: O(N)
    Set construction: O(N)
    Set comparison: O(N)
    => O(N) time
    => O(N) space
    """
    if len(str1) != len(str2):
        return False
    chars_map = defaultdict(int)
    for char in str1:
        chars_map[char] += 1
    for char in str2:
        chars_map[char] += 1
    return set(chars_map.values()) == {2}


if __name__ == '__main__':
    str1 = "Hello"
    str2 = "lolHe"
    print(permutation1(str1, str2))
