'''a=int(input("check even number or not?"))
if a%2==0:
    print (a," The given number is even")
else:
    print (a," The given number is odd ")
    

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def prin (self,name,age):
        #self.name=name
        #self.age=age
        print (f"Hello, my name is {name} and I am {age} years old.")

p2=person("rizwan",8)
p1=person("khan",44)
#p1.prin ("khan",36)
print (f"Hello, my name is {p2.name} and I am {p2.age} years old.")
print (f"Hello, my name is {p1.name} and I am {p1.age} years old.")

class dog:
    def __init__(self, name, age):
        self.name=name 
        self.age=age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
d1=dog("gimmy",4)
d2=dog("tommy",3)
print(d1)
print(d2)
print()
class Dog:
    # Class variable
    species = "Canine"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Access class and instance variables
print(dog1.species)  # (Class variable)
print(dog1.name)     # (Instance variable)
print(dog2.name)     # (Instance variable)
#
# Modify instance variables
dog1.name = "Max"
print(dog1.name)     # (Updated instance variable)

# Modify class variable
Dog.species = "Feline"
print(dog1.species)  # (Updated class variable)
print(dog2.species)
'''

#getter & setter Method
class student:
    def __init__(self):
        self.__firstname = "khan"
        self.__lastname = "jaffar"

    @property
    def Fullname(self):
        return self.__firstname + " " + self.__lastname
    
s=student()
print(s.Fullname)
print()

class Dog:
    def __init__(self, name, age):
        self.__name = name  # Conventionally private variable
        self.__age = age  # Conventionally private variable

    @property
    def name(self):
        return self.__name  # Getter

    @name.setter
    def name(self, value):
        self.__name = value  # Setter

    @property
    def age(self):
        return self.__age  # Getter

    @age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be negative!")
        else:
            self.__age = value  # Setter
d1=Dog("Lamberda",3)

print(d1.name)
print(d1.age)
print (f"the dog name is {d1.name} and age is {d1.age}")