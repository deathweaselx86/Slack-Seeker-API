from app.models import Tag
class Message:
    def __init__(self, url, description, tags, score, author, annotator):
        self.description = description
        self.score = score
        self.tags = []
        for tag in tags:
            self.tags.append(tag.name)
        self.url = url
        self.author = author
        self.annotator = annotator

    def __gt__(self, other):
        return other.score > self.score

    def __str__(self):
        return self.description + " " + self.score + " " + ' '.join(self.tags)

    def getScore(self):
        return self.score

    def setScore(self, score):
        self.score = score