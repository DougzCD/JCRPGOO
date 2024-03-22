from dog import Dog

mydog = Dog('Fox')
yourdog = Dog('Buddy')
mydog.add_trick('Roll Over')
yourdog.add_trick('Play Dead')
print(mydog.tricks)
print(yourdog.tricks)