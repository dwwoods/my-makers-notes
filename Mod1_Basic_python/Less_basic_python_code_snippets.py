# cheat_sheet.py
# A collection of Python snippets and explanations.

# ==============================================================================
# 1. LISTS - Ordered, mutable collections of items.
# ==============================================================================

print("--- LISTS ---")

# --- Creation ---
empty_list = []
fruits = ["apple", "banana", "cherry", "date"]
print(f"Initial list: {fruits}")

# --- Accessing & Slicing (zero-indexed) ---
first_fruit = fruits[0]       # "apple"
last_fruit = fruits[-1]       # "date"
slice_of_fruits = fruits[1:3] # ["banana", "cherry"] (index 1 up to, but not including, 3)
print(f"First fruit: {first_fruit}, Last fruit: {last_fruit}, Slice: {slice_of_fruits}")

# --- Adding Items ---
fruits.append("elderberry")   # Adds to the end
fruits.insert(1, "apricot")   # Inserts at a specific index
print(f"After adding: {fruits}")

# --- Removing Items ---
fruits.remove("banana")       # Removes the first occurrence of a value
popped_fruit = fruits.pop(2)  # Removes and returns item at index 2 ("cherry")
del fruits[0]                 # Deletes item at index 0 ("apple")
print(f"After removing: {fruits}, Popped: {popped_fruit}")

# --- Iteration & List Comprehension ---
print("Fruit names:")
for fruit in fruits:
    print(f"- {fruit}")

# A concise way to create lists
squared_numbers = [x**2 for x in range(5)] # [0, 1, 4, 9, 16]
print(f"Squared numbers: {squared_numbers}")


# ==============================================================================
# 2. DICTIONARIES - Unordered, mutable collections of key-value pairs.
# ==============================================================================

print("\n--- DICTIONARIES ---")

# --- Creation ---
empty_dict = {}
person = {
    "name": "Ada Lovelace",
    "occupation": "Mathematician",
    "born": 1815
}
print(f"Initial dictionary: {person}")

# --- Accessing & Updating ---
name = person["name"]                     # Access value by key
person["born"] = 1815                     # Update a value
person["died"] = 1852                     # Add a new key-value pair
print(f"Name: {name}, Updated dict: {person}")

# Safer access with .get() (returns None instead of an error if key doesn't exist)
birth_year = person.get("born")
death_year = person.get("died", "N/A") # .get() can also have a default value
print(f"Birth Year: {birth_year}, Death Year: {death_year}")

# --- Removing Items ---
age_at_death = person.pop("died") # Removes key and returns its value
del person["occupation"]          # Deletes a key-value pair
print(f"After removing: {person}, Age at death approx: {age_at_death - person['born']}")

# --- Iteration ---
print("Person details:")
for key, value in person.items():
    print(f"- {key.title()}: {value}")


# ==============================================================================
# 3. CLASSES & OBJECTS - Blueprints for creating objects.
# ==============================================================================

print("\n--- CLASSES ---")

# --- Basic Class Definition ---
# A class is a blueprint for creating objects (instances).
class Dog:
    # The __init__ method is the constructor, run when a new instance is created.
    # 'self' refers to the instance being created.
    def __init__(self, name, age):
        # Instance variables: data unique to each instance
        self.name = name
        self.age = age

    # A method: a function that belongs to the class
    def bark(self):
        return f"{self.name} says Woof!"

# --- Instantiation (Creating Objects) ---
# We create two separate instances of the Dog class.
dog1 = Dog("Rex", 5)
dog2 = Dog("Lucy", 3)

print(dog1.bark()) # Output: Rex says Woof!
print(f"{dog2.name} is {dog2.age} years old.") # Output: Lucy is 3 years old.

# --- Inheritance (A different use) ---
# A class can inherit attributes and methods from another class.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

# Cat inherits from Animal
class Cat(Animal):
    def speak(self): # This method overrides the parent's method
        return f"{self.name} says Meow!"

my_cat = Cat("Whiskers")
print(my_cat.speak()) # Output: Whiskers says Meow!


# ==============================================================================
# 4. SCOPE - Rules for where variables can be accessed.
# ==============================================================================

print("\n--- SCOPE ---")

# --- Global Scope ---
# This variable is accessible from anywhere in the script.
global_variable = "I am global"

class ScopeTester:
    # --- Instance Scope ---
    # This variable is tied to an instance of the class via 'self'.
    def __init__(self, name):
        self.instance_variable = name

    def test_scopes(self):
        # --- Local Scope ---
        # This variable only exists inside this method.
        local_variable = "I am local"
        print(f"Inside the method: {local_variable}")
        print(f"Method can access instance var: {self.instance_variable}")
        print(f"Method can also access global var: {global_variable}")

# Let's test the scopes
tester_object = ScopeTester("MyObject")
tester_object.test_scopes()

print(f"Outside, we can access the global var: {global_variable}")
print(f"Outside, we can access the instance var via the object: {tester_object.instance_variable}")

# This next line would cause a NameError because 'local_variable' only
# exists inside the 'test_scopes' method. It is forgotten once the method finishes.
# print(local_variable)