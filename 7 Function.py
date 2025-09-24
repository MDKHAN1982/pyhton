"""
def welcome():
    print("Welcome To Tutor Jaffar")
welcome()
welcome()

# No Return Type Without Argument Function in Python

def add():
    a=int(input("Enter The Value of A : "))
    b=int(input("Enter The Value of B : "))
    c=a+b
    print("Total ",c)
    
add()
# No Return Type With Argument Function in Python

def sub(a, b):
    c = a - b
    print("Difference : ", c)
  
sub(25, 2)
# Return Type Without Argument Function in Python

def mul():
    a = int(input("Enter The Value of A : "))
    b = int(input("Enter The Value of B : "))
    c = a * b
    return c
 
x=mul()
print("Mul ",x)
print()
# Arbitrary Arguments Function in Python (*)

def class_10(*students):
    print(students)
    for user in students:
        print(user)
 
class_10("allah", "mashallah", "subhanallah", "alhamdulila")

z = lambda  a ,b : a * b

print ("Mux value is :", z(11,33))

# Default Parameter Function in Python

def cust_details (name,age,city="periyakulam"):
    print ("Customer name is",name,"& his age is",age, "from ",city)

cust_details ("khan", 33)
"""
# Passing a List as an Argument in Function Python
def stud_tot(marks):
    return (sum(marks))

print ("total marks are :",stud_tot([1,2,3,4,5]))
