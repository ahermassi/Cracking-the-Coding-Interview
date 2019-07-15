import unittest2 as unittest

"""
Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string.
I wrote this code 30 minutes after I left the surgery room.
"""


def urlify(string, length):
    """ Replace single spaces with %20 and remove trailing spaces
    Time complexity: O(N)
    Space complexity: O(1): in-place
    """
    new_index = len(string)  # This is the actual length including trailing spaces to hold the additional character
    for i in reversed(range(length)):  # It's easiest to modify strings by going from the end of the string to the beginning
        if string[i] != ' ':
            string[new_index - 1] = string[i]  # Shift character to the end of string
            new_index -= 1
        else:
            string[new_index - 3:new_index] = '%20'  # Replace spaces
            new_index -= 3
    return string


class Test(unittest.TestCase):
    # Pass test strings as lists because Python's strings are immutable (can't assign to individual characters as
    # done in urlify()
    data = [
        (list('much ado about nothing      '), 22, list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))
    ]
    def test_urlify(self):
        for test_string, length, result in self.data:
            self.assertEqual(result, urlify(test_string, length))


if __name__ == '__main__':
    unittest.main()
