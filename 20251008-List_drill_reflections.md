# My Code Coaching Session Notes

**Date:** October 8, 2025

## My Goal for the Session

My goal was to review some of my Python functions and learn more professional and "Pythonic" ways to write them. I wanted to move beyond basic `for` loops to write cleaner and more efficient code.

---

## Key Things I Learned

### 1. Better Ways to Filter Lists

I started by using a standard `for` loop with an `if` statement to filter lists. I learned that while this works, there are better ways:

-   **List Comprehensions:** This seems to be the best and most common method. The syntax `[item for item in some_list if condition]` is really concise and easy to read once you get it.
-   **`filter()` function:** This is another good way, especially for more complex filters. `list(filter(lambda item: condition, some_list))` is a powerful pattern.

### 2. Transforming (Mapping) List Elements

For tasks like multiplying every number in a list, I learned the pattern is very similar to filtering.

-   Instead of a `for` loop, I can use a **list comprehension** to apply the transformation directly: `[num * some_number for num in some_list]`.

### 3. Custom Sorting with the `key` Argument

This was a big one. I learned that I don't need to write my own sorting algorithms from scratch.

-   The `sorted()` function is the tool to use.
-   By providing a `key` argument with a `lambda` function, I can tell `sorted()` exactly how to compare items, like sorting words by their last letter: `sorted(some_list, key=lambda word: word[-1])`.

### 4. Checking if All or Any Elements Match

I learned about two useful built-in functions for checking conditions across a whole list: `all()` and `any()`.

-   The best way to use them is with a **generator expression**, which is efficient and clean: `all(num > some_number for num in some_list)`.

---

## Important Core Concepts I Picked Up

1.  **In-Place Methods vs. Functions That Return a Value:** This was a huge takeaway. I realized that methods like `list.sort()`, `list.append()`, and `list.reverse()` change the list but return `None`, which was causing errors in my code. Functions like `sorted()` or operations like slicing (`[::-1]`) create and return a *new* object, which is what I usually need.

2.  **String Slicing:** I learned the `word[::-1]` trick, which is a very cool and simple way to reverse a string.

---

## New Habits to Build

-   **Use List Comprehensions First:** For filtering or transforming lists, I'll try to use a list comprehension as my default approach.
-   **Use `sorted()` with a `key`:** For any custom sorting task, this will be my go-to solution.
-   **Check Return Values:** I need to be more aware of what a method returns, especially if it's `None`.
-   **Use `all()` and `any()`:** For checks across a list, these are much cleaner than writing a manual loop.

Overall, this was a great session. I feel like I picked up these patterns quickly and can see how they'll make my code much better.