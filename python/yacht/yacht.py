# Score categories
# Change the values as you see fit
YACHT = 'YACHT'
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'


def score(dice, category):
    max_value = sorted(dice)[-1] # max value within the list
    total_score = 0 # total score
    set_dice = set(dice) # creates a set of the list dice

    if category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        for role in dice:
            if role == category:
                total_score += role
        return total_score

    elif category == 'CHOICE':
        return sum(dice)

    elif category == 'FULL_HOUSE':
        if len(set_dice) == 2:
            for value in set_dice:
                if dice.count(value) == 3:
                    total_score += (value * 3)
                elif dice.count(value) == 2:
                    total_score += (value * 2)
                else:
                    total_score = 0
            return total_score
        else:
            return total_score

    elif category == 'YACHT':
        if dice.count(max_value) == 5:
            return sum(dice)
        else:
            return total_score

    elif category == 'FOUR_OF_A_KIND':
        if len(set_dice) == 2 or len(set_dice) == 1:
            for value in dice:
                if dice.count(value) > 2:
                    return value * 4
        else:
            return total_score

    elif category == 'LITTLE_STRAIGHT':
        if len(set_dice) == 5:
            if sorted(dice)[0] == 1 & sorted(dice)[4] == 5:
                return 30
            else:
                return total_score
        else:
            return total_score

    elif category == 'BIG_STRAIGHT':
        if len(set_dice) == 5:
            if sorted(dice)[0] == 2:
                return 30
            else:
                return total_score

    elif category == 'YACHT':
        if len(set_dice) == 1:
            return sum(dice)
        else:
            return total_score