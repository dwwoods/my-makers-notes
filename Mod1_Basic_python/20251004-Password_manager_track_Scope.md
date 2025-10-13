# My Notes on Scope

Using the house / blueprint example from makerscourse/my-notes/20251004-Password_manager_track_classes.md

## Scope

Scope refers to the set of rules that determines where a variable can be accessed in your code. Variables can exist in different scopes, such as __global scope__ (accessible everywhere) or __local scope__ (accessible only within a specific function or class).

### 1. Global Scope 

*e.g. (The city)*

A variable in the global scope is like the street address of a house. It's defined outside of any class or function, and its value can be seen and accessed from anywhere in the program.

In our example, let's say all our houses are in the same `city`. This `city` variable is global.

```Python
# GLOBAL SCOPE
# 'city' is like the street address—visible to everyone.
city = "Metropolis"

class House:
    def __init__(self, address):
        # self.address belongs to the instance (see below)
        self.address = address

    def get_full_address(self):
        # This method can SEE the global 'city' variable.
        print(f"The house is at {self.address}, {city}.")

house_a = House("123 Maple St")
house_a.get_full_address() # Works perfectly

# We can also access 'city' directly from outside the class.
print(f"The entire development is in {city}.")
```
The `city` variable is accessible everywhere note its outside of the `class`

### 2. Instance Scope 

*e.g. (Inside the House)*

An instance variable is like the color of the paint on the walls inside the house. It's defined inside a class's methods (usually `__init__`) and belongs to a specific instance, attached by the `self` keyword.

To know the wall color, you have to specify which house you're talking about. You can't just ask, "What color are the walls?" You have to ask, "What color are the walls in `house_a`?"

```Python
class House:
    def __init__(self, address, color):
        # INSTANCE SCOPE
        # 'self.color' is like the paint color inside this specific house.
        self.address = address
        self.color = color

house_a = House("123 Maple St", "Blue")
house_b = House("456 Oak Ave", "White")

# To access the color, you MUST go through the instance.
print(f"House A's color is {house_a.color}.") # Correct!

# This will cause an error! It's like shouting on the street
# and expecting to know the wall color inside a house.
# print(f"The color is {color}.") # NameError: name 'color' is not defined
```
The variable `self.color` only exists within the context of a specific `House` instance.

### 3. Local Scope 

*e.g. A Conversation in a Room*

A variable in the __local scope__ is like a temporary thought or a secret told in one specific room of the house. It's created inside a method (and not attached to `self`), and it is __destroyed and forgotten__ as soon as the method finishes running.

Let's add a method to our ``House`` to do some temporary calculations.

```Python
class House:
    def __init__(self, address, color, area_sqft):
        self.address = address
        self.color = color
        self.area_sqft = area_sqft

    def calculate_tax(self, tax_rate_per_sqft):
        # LOCAL SCOPE
        # 'estimated_tax' is like a quick calculation on a notepad.
        # It only exists inside this 'calculate_tax' method.
        estimated_tax = self.area_sqft * tax_rate_per_sqft
        print(f"The estimated tax for this house is ${estimated_tax}.")
        # The 'estimated_tax' variable is accessible here.

house_a = House("123 Maple St", "Blue", 1500)

# The method works and uses its local variable just fine.
house_a.calculate_tax(0.5)

# This will cause an error! The 'estimated_tax' variable was
# forgotten as soon as the method finished.
# print(f"The tax is {estimated_tax}.") # NameError
```
The `estimated_tax` variable is temporary and only accessible inside the `calculate_tax` method where it was created.