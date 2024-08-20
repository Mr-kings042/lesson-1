favourite_number = 42
print(favourite_number)
print(f"My favourite number is {favourite_number}")

greeting = "Hello, world"
print(greeting)

is_python_fun = True
print(f"is_python_fun? {is_python_fun}")


# control flow

temperature = 30

if temperature > 24:
    print("it's hot outside")
elif temperature > 15:
        print('its warm outside')
else:
    print('its cold outside')
    print("the end")


    # loops(for and while)
for i in range(5):
     print(f"This is loop iteration {i}")
     # while loop
     i = 5
     while i > 5:
          print(f"Countdown: {i}")
          i -= 1
          print('blast off')

# functions
def greet(name):
     return f"Hello, {name}"
print(greet("John"))
print(greet("peter"))
# functions with arguments
def greet(name, age):
     return f"Hello, {name} you are {age} years old"
print(greet("John", 30))
# functions with default arguments
def greet(name, age=30):
     return f"Hello, {name} you are {age} years old"
print(greet("John"))
# functions with variable arguments
def greet(*args):
     return f"Hello, {args[0]} you are {args[1]} years old"
print(greet("John", 30))
     # functions with keyword arguments
def greet(**kwargs):
     return f"Hello, {kwargs['name']} you are {kwargs['age']} years old"
print(greet(name="John", age=30))
# functions with return values
def greet(name):
     return f"Hello, {name}"
print(greet("John"))
# functions with lambda
lambda name: f"Hello, {name}"("John")
# functions with recursion
def factorial(n):
     if n == 0:
          return 1
     else:
          return n * factorial(n-1)
print(factorial(5))


# lists
my_list = [1, 2, 3, 4, 5]
print(my_list[0]) 

fruits = ["apple", "banana", "orange"]
print(f"My favourite fruit is{fruits[0]}")

# dictionary 
person = {"name": "John", "age": 30, "city": "New York"}
print(person["name"])
print(f"John's age is {person['age']}")
# dictionary methods
person = {"name": "John", "age": 30, "city": "New York"}
print(person.keys())
    
# modules
import math
print(math.pi)

result = math.sqrt(144)
print(f" The square root of 144 is{ result}")


import module

print(module.function())
print(module.greet("kingsley"))
