# Object Oriented Programming in Python

'''
This file contains codes that has two class, Student and Course.
The Student class allows users to store information about a particular student, namely their name, age, and grade.
The Course class stores information about the class, namely the name and number of maximum students who can enroll in it.
The Course class also has a function/method called add_student that allows users to add students with the Student class into a list that does not exceed the maximum number of students.
It also has a method called get_average_grade that allows users to get the average grade of all students that are enrolled in a specific Course. 
'''

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def get_grade(self):
        return self.grade
    
    def get_name(self):
        return self.name

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        
        return value / len(self.students)

# Defining Students
s1 = Student("David", 23, 4.00)
s2 = Student("Carlos", 23, 3.00)
s3 = Student("Xaverius", 23, 3.08)
s4 = Student("Pardede", 23, 2.25)

# Defining Course
course = Course("Aerodynamics", 3)

# Adding Students to the Course
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

# Printing the Average Grade of all Students in the Course
print(course.get_average_grade())
    
