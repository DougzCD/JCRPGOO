from administrative_assistant import AdministrativeAssistant
from technical_assistant import TechnicalAssistant
from dog import Dog
from cat import Cat

def main():
    admin_assistant = AdministrativeAssistant("Alice", 101, 3000, "night", 500)
    tech_assistant = TechnicalAssistant("Bob", 102, 3500, 800)

    print("Administrative Assistant Details:")
    admin_assistant.display()
    
    print("\nTechnical Assistant Details:")
    tech_assistant.display()

    dog = Dog("Buddy", "Golden Retriever")
    cat = Cat("Whiskers", "Siamese")

    print("\nDog Details:")
    dog.display()
    dog.walk()
    dog.barks()

    print("\nCat Details:")
    cat.display()
    cat.walk()
    cat.meow()

if __name__ == "__main__":
    main()
