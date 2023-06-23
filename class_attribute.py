# Class Attributes
# Class Attributes are attributes that are specific to a class, not to an instance or object of that class.

# Defining a Class
class Person:
    number_of_people = 0    # This line defines an attribute that is general for the class, which means every object that is assigned to this class will have the same attributes.
    people = []
    
    def __init__(self, name):
        self.name = name
        Person.add_person()
    
    # The line below is called a decorator, which indicates that it is used to define a method for the class. The definition uses cls (Class) instead of self (Object)
    
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
    
    # The line below defines a static method, which applies for the whole code. It is useful to organize methods into a specific class.
    
    @staticmethod
    def show_number_of_people(x):
        print(x)
        
        
        
# Defining the Persons
p1 = Person("David")
p2 = Person("Carlos")
p3 = Person("Xaverius")
p4 = Person("Pardede")

# Showing the Number of People
Person.show_number_of_people(Person.number_of_people_())