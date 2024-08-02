from book import Book
from magazine import Magazine
from dvd import DVD
from cd import CD

def main():
    book = Book("The Great Gatsby", 1925, "F. Scott Fitzgerald", "9780743273565")
    magazine = Magazine("National Geographic", 2020, 12)
    dvd = DVD("Inception", 2010, "Christopher Nolan", 148)
    cd = CD("Thriller", 1982, "Michael Jackson", 9)

    print(book.display_info())
    print(magazine.display_info())
    print(dvd.display_info())
    print(cd.display_info())

if __name__ == "__main__":
    main()
