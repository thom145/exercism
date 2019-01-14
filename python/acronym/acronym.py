import re


def abbreviate(words):
    """
    :param words: the word you want the abbreviation of
    :return: returns the abbreviate as a string
    """
    list_abbreviate = re.split("[, \-!?:]+", words) # split on all given chars
    abbreviate = [word[0].upper() for word in list_abbreviate] # take the first letter of each word
    return ''.join(abbreviate)
