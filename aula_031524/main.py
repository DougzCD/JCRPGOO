from student import Student

nameStudent = input("Student name: ")
rollStudent = input("Student roll: ")
ageStudent = input("Student age: ")
qttGrades = int(input("Number of grades: "))
myStudent = Student(nameStudent, rollStudent, ageStudent, qttGrades)

print(myStudent.__str__())
print("\nTesting")
print(myStudent.name)
print(myStudent.getRoll())
print(myStudent._roll)
print(myStudent.getAge())
print(myStudent.__age)