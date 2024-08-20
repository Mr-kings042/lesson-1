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