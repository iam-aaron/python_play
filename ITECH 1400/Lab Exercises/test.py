class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print(self):
        print('Name: {}, age = {}'.format(self.name,self.age), end=' ')

class Student(Person):
    def __init__(self, name, age, ID):
        super().__init__(name, age)
        self.ID = ID
    def print(self):
        super().print()
        print(', Student ID: {}'.format(self.ID))


print("Create a person", end="\n\t")
person = Person('John Smith',25)
person.print()
print("\nCreate a student", end="\n\t")
student = Student('John Smith', 25, 30000000)
student.print()
print("Print a student as a person", end="\n\t")
Person.print(student)
print("\nPrint a student\'s type", end="\n\t")
print(type(student))
print("Running isinstance(student, Person)", end="\n\t")
print(isinstance(student, Person))
