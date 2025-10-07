# Chapter 2 Reflections

This chapter introduced some fundamental building blocks of Python: data structures and object-oriented programming with classes. Here are my thoughts on the key concepts.

***

## How do you create and add items to a List?

I learned that creating a list is as simple as using square brackets `[]`. You can create an empty list like `my_list = []` or initialize it with items like `my_list = ["apple", "banana"]`.

To add items, the **`.append()`** method is the most common way. It adds an item to the very end of the list. For example:

    fruits = ["apple", "banana"]
    fruits.append("cherry")
    # fruits is now ["apple", "banana", "cherry"]

If I need to add an item at a specific position, I can use the **`.insert()`** method, giving it the index and the item.

***

## How do you create and add items to a Dictionary?

Dictionaries are created using curly braces `{}` and store data as **key-value pairs**. For example, `my_car = {'make': 'Ford', 'model': 'Mustang'}`.

Adding a new item feels very intuitive. I just have to define a new key and assign a value to it, like this:

    my_car = {'make': 'Ford', 'model': 'Mustang'}
    my_car['year'] = 2022
    # my_car is now {'make': 'Ford', 'model': 'Mustang', 'year': 2022}

***

## List two differences between Lists and Dictionaries.

1.  **Accessing Elements**: The biggest difference for me is how I access elements. Lists are **ordered**, so I use an integer **index** (e.g., `my_list[0]`). Dictionaries are **unordered** (in principle) and use unique **keys** to access values (e.g., `my_dict['name']`). You can't ask for the "first" item in a dictionary in the same way.
2.  **Data Structure**: Lists are collections of individual items. Dictionaries are collections of **key-value pairs**. This makes dictionaries great for storing data that has a clear label or relationship, like the properties of an object.

***

## How do you define a class?

I define a class using the `class` keyword, followed by a name (usually in PascalCase). Inside the class, the **`__init__()`** method is the constructor. It's called automatically when a new object is created and is where I initialize its attributes. The `self` parameter is a reference to the specific instance of the class being created.

    class Dog:
      def __init__(self, name, breed):
        self.name = name
        self.breed = breed

***

## What is the difference between a class and an instance of a class?

My best analogy for this is a blueprint versus a house. 🏠

* A **class** is the **blueprint**. The `Dog` class defines the properties and behaviors that all dogs will have (e.g., a `name` and a `breed`).
* An **instance** is the actual **house** built from the blueprint. It's a specific, concrete object created from the class. For example, `my_dog = Dog("Rex", "German Shepherd")` creates an instance of the `Dog` class. There can be many instances (many different dogs), but they all follow the structure defined by the one class.

***

## What is meant by scope?

Scope determines where in a program a variable can be accessed. I learned there are two main types:

* **Local Scope**: A variable created inside a function is only accessible within that function.
* **Global Scope**: A variable created outside of any function can be accessed from anywhere in the code.

Understanding scope is crucial for avoiding `NameError` exceptions and for managing where data lives in a program. It helps prevent variables from different parts of the code from accidentally interfering with each other.