# Create a School class with instance attribute capacity.
# Add students as the class attribute. This will be a list and keep track of the students in the school.
# Create a Student class with attributes: name, age, gender
# Add __str__ method to this class to print the objects.
# Add add_student method to the class. If capacity is full print error message else add the student.
# Add print_students method to print the all existing students. 
# Loop through the students list and print each student object.
# Create a School object and threee students, add first 2 students to school. 
# Print students and afterwards try to add the third student.
# Use __dict__ method to see attributes

class School:
    
    students = []
    def __init__(self,capacity):
        self.capacity = capacity

    def add_student(self,student):
        if len(self.students)<self.capacity:
            self.students.append(student)
        else:
           print('Sorry! Capacity is Full...')

    def print_students(self):
        print(f"There are {len(self.students)} students. With following info:")
        for s in self.students:
            print(s)

class Student:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
                
    def __str__(self):
        return f" The name of student is {self.name}. Age : {self.age} Gender :{self.gender}"
    
school=School(2)   
student_1 = Student('John Snow','21','Male') 
student_2 = Student('Mary Gold','23','Female')
student_3 = Student('Mike Tyson','35','Male')
student_4 = Student('Michael Bean','32','Male')



school.add_student(student_1)
school.add_student(student_2)
school.print_students()
school.add_student(student_3)
print(school.__dict__)
print(student_1.__dict__)
print(student_2.__dict__)

