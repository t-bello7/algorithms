# # # another way, a class is like a form or questionnaire. An instance is like a form that has been filled out with information. 
# # Just like many people can fill out the same form with their own unique information, 
# # many instances can be created from a single class

# # The Dog class isn’t very interesting right now, so let’s spruce it up a bit by defining some properties that all Dog objects should have. 
# # There are a number of properties that we can choose from, including name, age, coat color, and breed. To keep things simple, we’ll just use name and age.

# # The properties that all Dog objects must have are defined in a method called .__init__().
# #  Every time a new Dog object is created, .__init__() sets the initial state of the object by assigning the values of the object’s properties.
# #  That is, .__init__() initializes each new instance of the class.


# class Dog:
    
#     # class attributes and they must be defined directly under the class
#     species = "Canis"
#     # this are instances attributes that are added to the class when instatiated

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # When writing your own classes, 
#     # it’s a good idea to have a method that returns a 
#     # string containing useful information about an instance of the class. 
#     # However, .description() isn’t the most Pythonic way of doing this

#     def __str__(self):
#         return('%s is %d'%(self.name, self.age))

#     #Instance methods are functions that are defined inside a class and 
#     # can only be called from an instance of that class. Just like .__init__(),
#     #  an instance method’s first parameter is always self.

#     def description(self):
#         return ('%s is %d years old'%(self.name, self.age))

#     #this instance method has the first parameter and the sound

#     def speak(self, sound):
#         return('%s says'%sound)

# rex = Dog("rex",2)
# timi = Dog("timi",4)
# print(rex.age)
# print(rex.speak('woof woof' ))

# print(rex.age)
# print(rex.speak('wooof' ))

# # You can simplify the experience of working with t
# # the Dog class by creating a child class 
# # for each breed of dog.

# # Remember, to create a child class, you create new 
# # class with its own name and then put the name of
# #  the parent class in parentheses


# class GermanSherpherd(Dog):
#     pass


# okay if you don't still grab let use Points
# Now you know a point can has two coordinatees 
# and can be anywhere in a space

class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2



p1 = Point(2,8)
print(p1.y)
print(p1.x)

p2 = Point(4,5)
print (p1.y)
print (p1.x)

def straight_line(input1, input2 ):
    E = (p2.y - p1.y) + (p1.x + p1.x)
    return E

E = straight_line(p1, p2)

print( 'equation of straight line is %s '%E)

class Flight():
    def __init__(self, capactiy):
        self.capacity = capactiy
        self.passengers = []

    def add_passenger(self, name):
        self.passengers.append(name)
    
    def open_seats(self):
        pass
flight = Flight(3)