class Message:
    def __init__(self, url, description, tags, score, author, annotator):
        self.description = description
        self.score = score
        self.tags = tags
        self.url = url
        self.author = author
        self.annotator = annotator

    def __gt__(self, other):
        return other.score > self.score

    def __str__(self):
        return self.description + " " + self.score

    def getScore(self):
        return self.score

    def setScore(self, score):
        self.score = score