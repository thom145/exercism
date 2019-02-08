import re
import collections

def word_count(phrase):
    phrase_cleaned = re.sub('[?|$.!,:%^&@_]', ' ', phrase) #removing all special char
    phrase_cleaned = [word.strip('\'"').lower() for word in phrase_cleaned.split()] #removing quotes

    return collections.Counter(phrase_cleaned)
