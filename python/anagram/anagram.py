from collections import Counter


def find_anagrams(word, candidates):
    for words in candidates:
        if words.lower() == word.lower():
            return []

    word_dict = Counter(word.lower())
    return [word for word in candidates if Counter(word.lower()) == word_dict]
