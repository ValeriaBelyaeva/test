from settings import figures

class Figur():
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self
        self.figur = figures[type]
    def drow(self):
