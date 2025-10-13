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


# --- 1. FizzBuzz: The "Specific Before General" Rule ---
# In an if/elif/else chain, always check the most specific condition
# first, as the chain stops executing after the first True match.
def fizz_buzz(number):
    if number % 15 == 0:
        return "fizzbuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return number

# --- 2. Greeting Reply: Exact vs. Contains ---
# Use an if/elif/else structure for a series of mutually exclusive checks.
# Use '==' for an exact match ("is").
# Use 'in' for a partial match ("contains").
def reply_to(greeting):
    if greeting == 'good morning':
        return 'good morning to you too'
    elif greeting == 'hello':
        return 'hi'
    else:
        return greeting

# --- 3. Simple Condition: The Ternary Operator ---
# For a simple if/else that returns a value, a ternary is a compact option.
# Format: value_if_true if condition else value_if_false
def deduct_10_if_possible(number):
    # Standard, clear approach:
    # if number >= 10:
    #     return number - 10
    # else:
    #     return number
    
    # Compact ternary version:
    return number - 10 if number >= 10 else number

# --- 4. Simple Condition: Using a Built-in Function ---
# Always look for a built-in function that does the job. It's often
# more readable and efficient. This logic is just finding the "max" value.
def top_up_to_100(number):
    # Standard, clear approach:
    # if number < 100:
    #     return 100
    # else:
    #     return number
    
    # The most Pythonic version using a built-in:
    return max(100, number)

# pythonic, Extensible Validator
# Use collections of functions for flexible rule-based systems.

def is_long_enough(password: str) -> bool:
    return len(password) >= 7

def has_special_character(password: str) -> bool:
    return any(char in "!@$%" for char in password)

VALIDATORS = [is_long_enough, has_special_character]

def is_valid_password(password: str) -> bool:
    # `all()` makes this clean and easy to extend via the VALIDATORS list.
    return all(validator(password) for validator in VALIDATORS)