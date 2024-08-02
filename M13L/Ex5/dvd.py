from collection import Collection

class DVD(Collection):
    def __init__(self, title, year, director, duration):
        super().__init__(title, year)
        self.director = director
        self.duration = duration

    def display_info(self):
        return f"DVD: {self.title}, Year: {self.year}, Director: {self.director}, Duration: {self.duration} minutes"
