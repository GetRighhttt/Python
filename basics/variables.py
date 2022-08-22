
name = "Stefan"  # String
age = 27  # Integer
gender = "Male"
pi = 3.14  # Float or Double
isAdult = True  # Boolean

"""
# Python is dynamically typed, so you don't have to explicitly
# state your variables, because its datatype is checked at run time.
# Variables are placeholders for data types, however in python,
# they aren't specified
"""

lastname, firstname = "Bayne", "Cool"  # We can also assign multiple variables with one line
# in Python

print(name, age, gender, pi, lastname, firstname, isAdult)
print((type(pi)))

# here is how we can explicitly state the type of variable that we are working with:
title: str = "GetRight"
print(title)


# Here is how we define method in python, needs two spaces afterwards also
def method() -> str:
    return "This is how we define a method in python."


"""
# Output: Stefan 20 Male 3.14 Bayne Cool
#  <class 'float'>
# GetRight
"""

