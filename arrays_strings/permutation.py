import unittest2 as unittest

"""
Given two strings, write a method to decide if one is a permutation of the
other.
"""
from collections import Counter


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
    chars_map = Counter(str1)  # dict holding count of characters in str1
    for char in str2:
        if chars_map[char] == 0:  # Character not found in str1
            return False
        chars_map[char] -= 1  # Decrement count to account for duplicate characters in the strings
    return True


class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_permutation(self):
        # True check
        for test_string1, test_string2 in self.dataT:
            self.assertTrue(permutation2(test_string1, test_string2))
        # False check
        for test_string1, test_string2 in self.dataF:
            self.assertFalse(permutation2(test_string1, test_string2))


if __name__ == '__main__':
    unittest.main()
