import random


class Character:
    @staticmethod
    def role_dice():
        """Role a dice 4 times and return the sum of the four largest value"""
        outcome = [random.randint(1, 6) for i in range(4)]
        outcome.sort() #sort in ascending order
        return sum(outcome[1:])

    def __init__(self):
        self.strength = self.role_dice()
        self.dexterity = self.role_dice()
        self.constitution = self.role_dice()
        self.intelligence = self.role_dice()
        self.wisdom = self.role_dice()
        self.charisma = self.role_dice()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        """Return a random ability from the character"""
        abilities = [self.strength, self.constitution, self.dexterity, self.intelligence,
                     self.wisdom, self.charisma, self.hitpoints]
        i = random.randint(0, 6)
        return abilities[i]


def modifier(constitution):
    """Return the constitution"""
    return (constitution - 10) // 2
