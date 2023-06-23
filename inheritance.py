# Inheritance

'''
Inspect the following blocks of code!

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        print("Bark")
        
Thera are wo classes with the name of Cat and Dog that is created on the lines above. 

But you may notice that both class looks very similar. In fact, the only difference is in the speak() function, which prints different strings.

You can save time and lines for such cases by using a concept of Inheritance.
'''

# Defining a Parent Class
# A Parent Class is a Class whose definitions will be inherited by a Child class.
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")
        
    def speak(self):
        print("I don't know what I say.")

# Defining a Child Class
# The Child Classes defined below (defined as class ChildClassName(ParentClassName)) will inherit all attributes existing in the Parent Class, but not limited to that. You can add additional attributes that will differ one Child Class from another.

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age) # This line calls the initial definition of the Parent Class with the corresponding arguments.
        self.color = color # This line adds another initial definition for the Child Class Cat.

    def speak(self):
        print("Meow")  # This line adds another method for the Child Class, that makes it unique from the other Child Class below.
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}.")
        # The above line modifies the show() function from the Parent Class, because it has another initial definition to print.

class Dog(Pet):
    def speak(self):
        print("Bark")
        
class Fish(Pet):
    pass
    # This Child Class do not have the unique speak() function, therefore, it will has the general function that the Parent Class has.

# Creating the Classes and calling out its functions

p = Pet("David", 23)
p.show()
p.speak()

c = Cat("Carlos", 23, "Black")
c.show()
c.speak()

d = Dog("Xaverius", 23)
d.show()
d.speak()

f = Fish("Pardede", 23)
f.show()
f.speak()

# Inheritance is useful for defining Classes that has similar attributes without retyping numerous, exactly same, lines of codes, which in turn can improve readability and efficiency of the code.

        
    