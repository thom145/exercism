class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def personal_best(self):
        return sorted(self.scores)[-1]

    def latest(self):
        return self.scores[-1]

    def personal_top(self):
        return sorted(self.scores, reverse=True)[:3]

    def report(self):
        max_value = sorted(self.scores)[-1]
        latest_value = self.scores[-1]
        if max_value == latest_value:
            return "Your latest score was {}. That's your personal best!".format(latest_value)
        else:
            return "Your latest score was {}. That's {} short of your personal best!".format(latest_value, (max_value-latest_value))


