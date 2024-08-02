class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def display(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")

    def walk(self):
        print(f"{self.name} is walking.")
