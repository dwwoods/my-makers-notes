# My Notes on Python Classes

**HARD**
## Reflecting 
*4 Oct 2025* 
*updated on 10 Oct 2025 after the Workshop* 
I dont get this. First I'll try to EIL5

### Eli5

* Purpose: The main purpose of classes is to bundle related data and functions together into reusable blueprints for creating objects. Think of them as a way to organize and structure your code in a logical, real-world way

* A class is essentially a template for creating things. It defines two key aspects of an object:

    `Attributes`: The data or properties that the object has.

    `Methods`: The functions or actions that the object can do.

* Reusability and Consistency Once you've defined the blueprint (the class), you can create many individual, unique objects from it. Each object is called an `instance`. Following the car example, you could use your single Car class to create many different car instances:

    * `my_car = Car("Red", 120)`
    * `friends_car = Car("Blue", 150)`

    Both my_car and friends_car are separate objects with their own unique attributes (red vs. blue), but they were built from the same consistent blueprint and share the same methods. This is incredibly efficient because you don't have to rewrite the code for every new car you want to create. This follows the DRY (Don't Repeat Yourself) principle in programming.

* Encapsulation is the practice of bundling an object's data (attributes) and the methods that operate on that data together within the class. A key part of this is that the object's internal state is often "hidden" from the outside.

### Mental Model


Think of a __class__ as an architect's blueprint for a house. The blueprint defines the structure—how many rooms, where the doors are, etc.—but it's not a house you can live in. 

An __instance__ is an actual, physical house built from that blueprint.

* __Class__ (Blueprint): Defines the attributes (e.g., color, address) and methods (e.g., paint_house()).

* __Instance__ (The House): A single, usable object created from the blueprint.

You create an instance by "calling" the class name as if it were a function. This process is called instantiation. When you do this, a special constructor method (usually __init__ in Python) runs automatically to set up the instance's initial state.

This is like the construction crew taking the blueprint and building the house at a specific address with an initial coat of paint.


## Here's my attempt at explaining Python classes using the cookie analogy. 

What is a class?
A class is the blueprint or the cookie cutter. It's not a cookie itself, but it's the template that defines what a cookie will look like and what it can do. It holds the design for all the cookies I'm going to make.

```Python

# This is the blueprint. It defines what a cookie is.
class Cookie:
    # A class can be empty to start with.
    pass
```

### How is a class defined?
I define a class using the class keyword, followed by a name (which I'll capitalize, like Cookie), and a colon. Everything that's part of the blueprint is indented underneath it.

```Python

# Here, I'm defining the blueprint for my cookie.
# I've designed it to have an 'eat' action.
class Cookie:
    def eat(self):
        return "Nom nom nom!"
```

### What is an instance of a class?
An instance is an actual cookie that I've made using the cookie cutter. It's a real, tangible object that was created based on the class blueprint. I can make lots of different instances (cookies) from just one class (the cookie cutter).


```python

# The 'Cookie' class is the cutter.
# 'my_cookie' is an actual cookie—an instance.
my_cookie = Cookie()
```

### How is a class instantiated?
I instantiate a class by calling the class name like it's a function, using parentheses (). This action is like pressing the cookie cutter into the dough; it creates a new, separate cookie object in memory.

```Python

# I'm "instantiating" the Cookie class to create two separate cookies.
# Each one is its own object.
cookie1 = Cookie()
cookie2 = Cookie()
```
### What is an instance variable?
An instance variable is a property that is unique to each cookie. For example, one cookie's flavor can be "chocolate", while another's is "vanilla". These variables hold the specific state of each individual instance.


```Python

# In this blueprint, 'self.flavor' will be the instance variable.
class Cookie:
    def __init__(self, flavor):
        # Every cookie will have its own flavor.
        self.flavor = flavor
```

### How are instance variables assigned?
I assign instance variables inside the __init__ method (the constructor). When I create a new cookie, I pass in the values I want (like the flavor). The __init__ method then uses the self keyword to attach those values to that one specific cookie being created. self.flavor = flavor means "Take the flavor I was given and store it as this specific cookie's flavor."


```Python
class Cookie:
    # This method runs automatically when a cookie is created.
    def __init__(self, shape, flavor):
        # 'self.shape' and 'self.flavor' are the instance variables.
        # They get their values from the arguments passed in during instantiation.
        self.shape = shape
        self.flavor = flavor

# I instantiate a cookie, passing in "star" and "sugar".
# Inside __init__, self.shape becomes "star" and self.flavor becomes "sugar" for this cookie.
star_cookie = Cookie("star", "sugar")

# I can access that cookie's unique instance variables.
print(f"I made a {star_cookie.shape} cookie with a {star_cookie.flavor} flavor.")
# Output: I made a star cookie with a sugar flavor.
```
## Summary 
I did not enjoy this. 

In essence. you define the class. decide what happens when you encapsulate with `__init__` this define the attributes (data) and then decide what we can do with to that object with methods i.e. further `def`

