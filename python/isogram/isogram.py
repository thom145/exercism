from collections import Counter
import re


def is_isogram(string):
    string = re.sub(r'[^\w\s]', '', string.lower()).replace(' ', '')
    return len(string) == len(Counter(string).items())