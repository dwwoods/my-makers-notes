# Python Refactoring Reflections 
    See makerscourse/my-notes/20251002-Python_password_validator_challenge_reflections.md 

The Challenge was:

```Python
# == INSTRUCTIONS ==
#
# Purpose: Validate a password
# Parameters: one, a string
# Rules:
#   - It must be longer than 7 characters (8 is fine)
#   - It must contain at least one of the following special characters: `!`, `@`,
#     `$`, `%` or `&`
# Returns: a boolean (True if valid, False otherwise)
# Example:
#   Call:    is_valid("1234567")
#   Returns: False
#   Call:    is_valid("12345678")
#   Returns: False
#   Call:    is_valid("12345!78")
#   Returns: True
```

My solution was:

```Python
def is_valid(password):
    special_char = ('!', '@', '$', '%', '&')
    length_8 = False
    has_special_char = False
    if len(password) >= 8:
        length_8 = True
    for char in password:
        if char in special_char:
            has_special_char = True
    if length_8 == True and has_special_char == True:
        return True
    else:
        return False
```

The refactored suggestion from the docs looks like this:

```Python
def is_sufficient_length(password):
  # len(password) > 7 will evaluate to True or False
  return len(password) > 7


def are_special_chars_included(password):
  if "!" in password:
    return True
  elif "@" in password:
    return True
  elif "$" in password:
    return True
  elif "%" in password:
    return True
  elif "&" in password:
    return True
  else:
    return False


def is_valid(password):
  if is_sufficient_length(password) and are_special_chars_included(password):
    return True
  else:
    return False


```
## Refactoring

### What is it?
    refactoring is the disciplined process of restructuring existing computer code—changing the internal structure—without changing its external behavior. It's not about adding new features; it's about cleaning up the code you already have to fight "technical debt."

### Why do it? 
    The primary benefit of this practice is maintainability. Refactored code is simpler to read, easier to debug, and safer to extend. By investing time in improving the design, you make the entire system more robust and reduce the cost and effort of future development. It transforms a rigid, fragile codebase into one that is flexible and resilient to change.

### Why is the refactored code better?
    By decoupling the high-level logic from the low-level database details. This design is far superior because it's flexible—you can swap the database without touching the core reminder logic—and much easier to test. 

## SOLID Principles

### S: Single Responsibility Principle (SRP) 
    A class should be responsible for only one part of the system's functionality. This means it should have only one reason to change. Concentrating on a single task makes the code more robust and easier to understand.

### O: Open/Closed Principle (OCP) 
    Software entities should be open for extension, but closed for modification. You should be able to add new features without changing existing, proven code. This is typically achieved by using abstractions like interfaces or abstract classes.

### L: Liskov Substitution Principle (LSP) 
    Objects of a superclass should be replaceable with objects of a subclass without affecting the program's correctness. A subclass must honor the contract of its parent class, ensuring predictable behavior. This is fundamental to building reliable class hierarchies.

### I: Interface Segregation Principle (ISP) 
    A client should not be forced to depend on interfaces it does not use. It's better to have many small, specific interfaces than one large, general-purpose one. This prevents "fat" interfaces and keeps the system decoupled.

### D: Dependency Inversion Principle (DIP) 
    High-level modules should not depend on low-level modules; both should depend on abstractions. This principle inverts the traditional dependency flow, promoting loose coupling. It's often implemented using dependency injection to make code more flexible.

## Applying the principles to my code

```Python
def is_long_enough(password):
    return len(password) >=8


def has_special_character(password):
    special_char = ('!', '@', '$', '%', '&')
    for char in password:
        if char in special_char:
            return True
        else:
            return false


def is_valid(password):
  if is_long_enough(password) and has_special_character(password):
    return True
  else:
    return False

```
## A more pythonic way of doing it is:

go team pine. 

```Python
def is_long_enough(password):
    """Checks if the password is at least 7 characters long."""
    return len(password) > 7


def has_special_character(password):
    """Checks for the presence of at least one special character."""
    special_chars = {'!', '@', '$', '%', '&'} # A set is faster for lookups
    return any(char in special_chars for char in password)


def is_valid(password):
  """Checks if a password meets all validity criteria."""
  return is_long_enough(password) and has_special_character(password)


```
