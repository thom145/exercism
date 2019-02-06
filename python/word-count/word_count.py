import re
import collections

def word_count(phrase):
    phrase_cleaned = re.sub(r'[?|$|.|!|,|:|%|^|&|@|_]', r' ', phrase) # removing all special char
    phrase_cleaned = [word.strip('\'"').lower() for word in phrase_cleaned.split()] # removing quotes

    return dict(collections.Counter(phrase_cleaned))
