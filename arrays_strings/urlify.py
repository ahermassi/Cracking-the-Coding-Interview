"""
Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string.
I wrote this code 30 minutes after I left the surgery room.
"""


def urlify(str):
    words = str.split()
    return '%20'.join(words)


if __name__ == '__main__':
    str = 'Mr John Smith  '
    print(urlify(str))
