# My Python Notes: Advanced Dictionaries

## ## 1. What is a Dictionary?

A dictionary is a collection that stores data in **key-value pairs**. The key must be unique and is used to look up its associated value. This is different from a list, where items are ordered and accessed by a numerical index (their position).

-   **Lists**: Use when the **order** of items matters.
-   **Dictionaries**: Use when the **relationship** between items matters.

    # 'name' and 'role' are keys
    user = {'name': 'Alice', 'role': 'Developer'}

    # Access the value using its key
    user['role'] # Returns 'Developer'

## ## 2. Manipulating Dictionaries

### ### Creating Dictionaries: Comprehensions

Dictionary comprehensions are a concise and **Pythonic** way to create a new dictionary by iterating over an existing dictionary or another iterable. They are generally preferred over `for` loops for this task.

**Syntax:** `{new_key: new_value for key, value in dict.items() if condition}`

    # Example 1: Transform values (create a new dict with scores out of 10)
    scores = {'Alice': 88, 'Bob': 45, 'Charlie': 92}
    scores_out_of_10 = {name: score / 10 for name, score in scores.items()}
    # Result: {'Alice': 8.8, 'Bob': 4.5, 'Charlie': 9.2}

    # Example 2: Filter items (create a new dict with only passing scores)
    passing_scores = {name: score for name, score in scores.items() if score >= 50}
    # Result: {'Alice': 88, 'Charlie': 92}

### ### Safely Accessing Keys: `.get()`

Using square brackets `my_dict['key']` to access a key that doesn't exist will raise a `KeyError`. The `.get()` method is a safer way to access keys.

-   `my_dict.get('key')`: Returns the value if the key exists, otherwise returns `None`.
-   `my_dict.get('key', 'default_value')`: Returns the value if the key exists, otherwise returns `'default_value'`.

    user = {'name': 'Alice'}
    user.get('role') # Returns None
    user.get('role', 'Viewer') # Returns 'Viewer'

### ### Merging Dictionaries: `.update()` or `|`

The best use for the `.update()` method is to merge one dictionary into another.

    user_profile = {'name': 'Alice', 'username': 'alice_a'}
    user_permissions = {'role': 'editor', 'level': 3}
    user_profile.update(user_permissions)
    # user_profile is now {'name': 'Alice', 'username': 'alice_a', 'role': 'editor', 'level': 3}

In Python 3.9+, you can also use the `|` operator for a cleaner look:

    merged_dict = user_profile | user_permissions

### ### Removing Items: `.pop()`

The `.pop('key')` method removes a key-value pair from the dictionary and, importantly, returns the value that was removed.

    user = {'name': 'Alice', 'role': 'Developer'}
    removed_role = user.pop('role')
    # removed_role is 'Developer'
    # user is now {'name': 'Alice'}

## ## 3. What is "Pythonic"?

"Pythonic" code values **readability and expressiveness**. For tasks like creating a new collection from an existing one, advanced methods like **comprehensions** are considered more Pythonic than simple `for` loops.

-   A **`for` loop** describes the *step-by-step process* of building the dictionary.
-   A **comprehension** describes *what the final dictionary should look like*.

While a simple loop is never wrong, using the language's built-in, expressive tools is a key feature of the Pythonic style.