# My Python Notes: Advanced List Operations

## ## 1. Three Ways to Process Lists

There are several ways to search for items or create new lists from existing ones. We explored three main approaches: manual `for` loops, functional tools like `filter()` and `map()`, and Pythonic list comprehensions.

### ### A. The "Classic" Way: `for` Loops

#### #### Searching with `for` and `if`
This is the foundational method. You iterate through each item and use an `if` statement to see if it matches a condition.

    # Find all numbers greater than 5
    numbers = [1, 8, 3, 10, 5, 2]
    large_numbers = [] 

    for number in numbers:
      if number > 5:
        large_numbers.append(number)

#### #### Transforming with `for`
To create a new list where each element is modified, you loop through the original, perform an operation, and append the new value to a new list.

    # Create a list of doubled numbers
    numbers = [1, 2, 3, 4]
    doubled_numbers = []

    for number in numbers:
      doubled_numbers.append(number * 2)

### ### B. The Functional Way: `filter()`, `map()`, and `lambda`

#### #### `filter()`
The built-in `filter()` function is a concise alternative to a `for`/`if` loop for searching. It takes a function and a list, and returns an iterator with only the items for which the function returned `True`.

    def is_even(num):
      return num % 2 == 0

    numbers = [1, 2, 3, 4, 5, 6]
    even_numbers = list(filter(is_even, numbers))

#### #### `lambda` Functions
A `lambda` function is a small, anonymous function. They are perfect for using with `filter()` and `map()` when you don't want to define a separate, full function.

**Syntax:** `lambda arguments: expression`

    numbers = [1, 2, 3, 4, 5, 6]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

A practical example is finding a specific dictionary in a list. The `next()` function is useful here to efficiently get just the first match.

    passwords = [
       {'service': 'acebook', 'password': 'password123'},
       {'service': 'makersbnb', 'password': 'qwerty789'}
    ]

    acebook_entry = next(filter(lambda p: p['service'] == 'acebook', passwords), None)

#### #### `map()`
The `map()` function is the functional alternative for transforming a list. It applies a function to every item in a list.

    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x * x, numbers))

### ### C. The Pythonic Way: List Comprehensions

List comprehensions are often the most readable and preferred way to create new lists from existing ones in Python. They combine the loop, condition, and expression into one line.

**Syntax:** `[expression for item in iterable if condition]`

    numbers = [1, 2, 3, 4, 5, 6]
    evens = [num for num in numbers if num % 2 == 0]

    squares = [num * num for num in numbers]

You can even combine filtering and transforming.

    passwords = [
       {'service': 'acebook', 'added_on': '22/03/22'},
       {'service': 'makersbnb', 'added_on': '22/03/22'},
       {'service': 'twitter', 'added_on': '21/03/22'}
    ]

    services = [p['service'] for p in passwords if p['added_on'] == '22/03/22']

---

## ## 2. Core Python Concepts

### ### `print()` vs. `return()`
- **`print()`**: Displays a value to the human user in the terminal. The function's output cannot be used by the rest of the program. Its actual return value is `None`.
- **`return`**: Gives a value back from a function to the code that called it. This value can be stored in a variable and used for further operations.

### ### Scope
Scope defines where a variable can be accessed.
- **Local Scope**: Variables created inside a function only exist within that function.
- **Global Scope**: Variables created outside of any function are global and can be accessed from anywhere, but it's best to avoid relying on them inside functions.

---

## ## 3. Practical Code Examples (Fixed)

### ### Checking a Condition for All Items
The goal was to check if all passwords in a list were long enough (e.g., >= 8 characters). The logic is to `filter` for any passwords that are **too short**. If the resulting list is empty (`== []`), then all passwords must have been long enough.

    def are_all_passwords_long_enough(passwords):
        min_length = 8
        short_passwords = list(
            filter(
                lambda p: len(p['password']) < min_length,
                passwords
            )
        )
        return short_passwords == []

### ### Finding Items by a Property
The goal was to find all passwords added on a specific date. This involves fixing variable shadowing and using the correct lambda logic (comparison).

    def find_passwords_added_on(date_to_find):
        return list(
            filter(
                lambda password: password['added_on'] == date_to_find,
                passwords
            )
    