# Python Cheat Sheet

# --- Strings ---
# A string is a sequence of characters, created with single or double quotes.
my_string = "Hello, World!"
another_string = 'Python is fun.'

# You can join strings (concatenate) using the + operator.
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name  # Results in "Hello, Alice"


# --- String Methods ---
# Methods are actions you can perform on an object, like a string.

# .upper() and .lower() to change case.
print(my_string.upper())  # Output: HELLO, WORLD!
print(my_string.lower())  # Output: hello, world!

# .replace() to find and replace a substring.
print(my_string.replace("World", "Python")) # Output: Hello, Python!

# .strip() to remove whitespace from the beginning and end.
padded_string = "   some text   "
print(padded_string.strip()) # Output: some text

# f-strings for easy formatting.
age = 30
formatted_string = f"The user is {age} years old."
print(formatted_string) # Output: The user is 30 years old.


# --- Conditionals (Making Decisions) ---
# if, elif, else statements control which code runs based on a condition.
temperature = 25

if temperature > 30:
    print("It's a hot day.")
elif temperature > 20:
    print("It's a pleasant day.") # This block will run
else:
    print("It might be cold.")


# --- Flow Control (Loops) ---

# A 'for' loop iterates over a sequence (like a list or a range).
# This loop prints numbers 0 through 4.
for i in range(5):
    print(f"For loop iteration: {i}")

# A 'while' loop continues as long as a condition is True.
# This loop also prints numbers 0 through 4.
count = 0
while count < 5:
    print(f"While loop iteration: {count}")
    count = count + 1 # Increment the counter to avoid an infinite loop!


# --- Defining and Calling Functions ---

# Use 'def' to define your own function.
# This function takes two numbers and returns their sum.
def add_numbers(a, b):
    """This is a docstring, explaining the function."""
    return a + b

# To use the function, you "call" it with arguments.
sum_result = add_numbers(5, 10)
print(f"The result of the function is: {sum_result}") # Output: 15

# Functions don't have to return anything.
def say_hello(person_name):
    print(f"Hello, {person_name}!")


# Calling a function that prints directly.
say_hello("Bob") # Output: Hello, Bob!
