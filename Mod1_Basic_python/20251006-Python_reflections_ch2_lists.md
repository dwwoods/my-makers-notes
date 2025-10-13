# My Coding Session Notes & Reflections
Date: 06 October 2025

__makerscourse/python_chapter_2_challenges/drills/lib/_1_lists_and_dictionaries.py__

Today, I worked through a series of fundamental Python problems. The goal was to implement basic list operations from scratch and learn about common bugs and best practices along the way.

## Core Concepts & Early Lessons
Problem: `total(list)`
My first task was to sum all the numbers in a list. My initial code had a critical indentation error where the `return` statement was inside the `for` loop, causing the function to exit prematurely.

Key Learnings
Indentation is critical: In Python, indentation defines code blocks. A misplaced `return` completely changes the logic.

Pro Tip: It's bad practice to name variables after built-in types (like `list`). I should use names like `num_list`.

The Pythonic Way: The built-in sum() function is the best and simplest way to do this.

## Problem: `first_element(num_list):`
This function was straightforward: return the first element. My initial solution was return `num_list[0]`.

### Issue: Edge Cases
The big lesson here was about edge cases. My code would crash with an `IndexError` if given an empty list `[]`. This introduced me to the idea of writing "defensive code" by adding a "guard clause" at the top of the function to check for bad inputs.

### The Fix

```Python
def first_element(num_list):
    if not num_list:
        return None
    return num_list[0]
```

## Problem: `lowest_number()` & `highest_number()`
These problems required finding the min/max value. My first attempt at `lowest_number` failed with a `TypeError` because I initialized the tracking variable with a tuple `()` instead of a number.

### The Fix & Refinements
Smart Initialization: I learned that the best way to start is to assume the first element is the lowest/highest: `lowest = num_list[0]`.

Handling Edge Cases: 
This brought back the empty list problem, so I added the `if not num_list:` check here as well.

Efficiency Tweak: 
To avoid a redundant check, I learned to loop over the rest of the list by using a slice: `for i in num_list[1:]`.

The Pythonic Way: 
The built-in `min()` and `max()` functions are the right tools for the job.

## Function Interaction & List Methods

### Problem: `the_beatles()` & Function Calls
This set of problems focused on function definitions, return types, and how functions interact.

#### Key Learnings
Syntax Matters: I learned the difference between creating a list `[]` and a tuple `()`.

Function Definitions: The parentheses in a function definition are for naming arguments. If there are no arguments, they should be empty: `def my_func():`.

Variable Scope: A variable created inside one function isn't visible in another. To use a result from `the_beatles()` inside another function, I had to call it `the_beatles()` and store its return value.

List Methods: I learned the difference between `.append()` (adds one item) and `.extend()` (adds all items from another list). I also learned that `.append()` modifies a list but returns None, which is a common trap.

## Data Cleaning & Uniqueness

### Problem: `remove_nones_from_list()`
The goal was to remove all `None` values from a list. My first attempts failed because I was checking for the string `"None"` instead of the keyword `None` and trying to add items to a list with `+` instead of `.append()`.

#### Key Learnings
`None` is a keyword: To check for it, the correct syntax is `if item is not None`.

Use `.append():` The proper way to add a single item to a list is with the `.append()` method.

List Comprehensions: A more advanced and readable way to solve this is with a list comprehension: `[item for item in items if item is not None]`.

## Problem: `unique_elements()`
Here I needed to remove duplicate elements from a list. My initial logic was flawed because I was checking `if element is not uniques` instead of if `element not in uniques`.

### The Power of Sets
The biggest takeaway was learning about sets. A set is an unordered collection of unique items. By converting a list to a set and back to a list, I can remove duplicates in one clean, efficient line of code.

```Python
def unique_elements(elements):
    return list(set(elements))
```

### Problem: `Notes()`
The final drill was to add an element to a list. My solution return `elements + extra_element` was incorrect because you can't add a list and a non-list item together. Although this did pass the pytest... 

#### Key Learnings
Mutation vs. Creation: I learned the difference between changing an original list (`.append()`) and creating a new one (`+`).

Correct Concatenation: To add items using +, both operands must be lists. The fix was to wrap the new item in a list: return elements + [extra_element].

Conclsion: 

* I need to learn how to be more concise i.e 
```python
return [item for item in items if item is not None]
```
* Think about Edge Cases: The most important lesson was to always think "how could this break?". The empty list `[]` is a classic and common edge case.

* Embrace Pythonic Solutions: For many common tasks, Python has a built-in function (`sum()`, `min()`, `max()`) or a preferred structure (list comprehensions, sets) that is cleaner, faster, and less error-prone.

* Need more practice with sets. 
