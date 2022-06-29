# Create a Python class Person with attributes: name and age of type string.
# Create a display() method that displays the name and age of an object created via the Person class.
# Create a child class Student which inherits from the Person class and which also has a section attribute.
# Override the method display() for the Student class. 
# Make it such that it displays the name, age and section of an object created via the Student class.
# Create Person and Student objects and then test the display() method for both.
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print('Name of the Person is',self.name)
        print('Age of the Person is',self.age)

class Student(Person):
    def __init__(self,name,age,section):
        super().__init__(name,age)
        self.section = section

    def display(self):
        print('Name of the Student is',self.name)
        print('Age of the Student is',self.age)
        print('Section of the Student is',self.section)

newPerson = Person('Jessica Janes',18)
newPerson.display()
newStudent = Student('Mary Jones',24,'Science')
newStudent.display()
