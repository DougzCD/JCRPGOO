class Student:

    def __init__(self, name, number):
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)
            
    def __str__(self) -> str:
        return "Name:" + self.name + "/nScores:" + \
            " " .join(map(str, self.scores))
            
    def getName(self):
        return self.name
        