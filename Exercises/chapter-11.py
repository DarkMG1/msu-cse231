# q1
class Student():
    def __init__(self, score=10):
        self._score = score

    def add_score(self):
        self._score += 10

    def decrease_score(self):
        self._score -= 10

    def __str__(self):
        return str(self._score)

# q2
class RockGuitars:
    def __init__(self):
        self._guitarist = ""
        self._guitar = ""

    def add_entry(self, guitarist="", guitar=""):
        self._guitarist = guitarist
        self._guitar = guitar

    def __str__(self):
        return "{:<20s} {:<20s}".format(self._guitarist, self._guitar)