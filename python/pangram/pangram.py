def is_pangram(sentence):
    """
    Check if a sentence is a pangram
    returns the number of unique letters
    """

    words = ''.join(sentence.split()) #remove all spaces from the sentence
    unique_letters = {letter.lower() for letter in words}  #add all the letters to a dictionary
    return unique_letters == 26

print(is_pangram('hello how are you'))