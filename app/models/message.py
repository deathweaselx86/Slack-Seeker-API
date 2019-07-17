class Message:
    def __init__(self, text, score, tags):
        self.text = text
        self.score = score
        self.tags = tags

    def __gt__(self, other):
        return other.score > self.score

    def __str__(self):
        return self.text + " " + self.score

    def returnScore(self):
        return self.score