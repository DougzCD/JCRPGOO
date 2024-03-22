class Store:
    tax = 1.03
    seila = 'seila'

    def __init__(self, address) -> None:
        self.__address = address

    def showAddress(self):
        print(self.__address)

    @staticmethod
    def a(text):
        seila = text
        print(seila)

    @classmethod
    def sell(cls):
        return 100 * cls.tax
    
    @classmethod
    def setTax(cls, newTax):
        cls.tax = newTax