import re


def word_count(phrase):
    phrase_cleaned = re.sub(r'[?|$|.|!|,|:|%|^|&|@|_]', r' ', phrase) # removing all special char
    phrase_cleaned = [word.strip('\'"') for word in phrase_cleaned.split()] # removing quotes

    all_words = {}

    for word in phrase_cleaned:
        if word.lower() not in all_words.keys():
            all_words[word.lower()] = 1
        else:
            all_words[word.lower()] += 1

    return all_words
