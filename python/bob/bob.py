import re


def hey(phrase):
    def check_if_all_caps(phrase):
        if len(phrase) > 0:
            return phrase == phrase.upper()
        else:
            return False

    def check_for_special(phrase):
        if phrase.split()[-1][-1] == '!' or phrase.split()[-1][-1] == '?':
            return phrase.split()[-1][-1]


    cleaned_phrase = re.sub('[^a-zA-Z]+', '', phrase)
    if check_if_all_caps(cleaned_phrase):
        if check_for_special(phrase) == '?':
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif len(phrase.split()) == 0:
        return "Fine. Be that way!"
    elif phrase.split()[-1][-1] == '?':
        return 'Sure.'
    else:
        return "Whatever."

