from collection import Collection

class Book(Collection):
    def __init__(self, title, year, author, isbn):
        super().__init__(title, year)
        self.author = author
        self.isbn = isbn

    def display_info(self):
        return f"Book: {self.title}, Year: {self.year}, Author: {self.author}, ISBN: {self.isbn}"
