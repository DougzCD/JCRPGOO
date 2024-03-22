from store import Store

store1 = Store('Comandathuba Beach')
store2 = Store('Shopping')

store1.showAddress()
print(store1.sell())
print(store2.sell())

store1.setTax(1.5)

print(store1.sell())
print(store2.sell())

Store.setTax(2.0)

print(store1.sell())
print(store2.sell())

Store.a('b')
store1.a('c')
print(store1.seila)
print(store2.seila)