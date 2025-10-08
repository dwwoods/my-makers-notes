# My Dictionary Session Notes

## My Goal

Following up on lists, my goal for this session was to get comfortable with Python dictionaries and learn the most common, "Pythonic" ways to work with them, moving beyond basic loops.

---

## Key Things I Learned

### 1. Using Built-in Functions is Better

My first instinct for summing values was to write a `for` loop. I learned that Python often has a built-in function that is faster and more readable.

-   **For summing values:** `sum(my_dict.values())` is much cleaner than a manual loop.

### 2. The Best Way to Add, Update, and Remove

-   **Adding/Updating:** For a single item, `my_dict[key] = value` is the most direct and common way. The `.update()` method I was using is better for merging another dictionary.
-   **Removing:** My use of `my_dict.pop(key)` was correct. I learned `del my_dict[key]` is an alternative if I don't need the removed value.
-   **Safe Removals:** A huge takeaway was how to avoid `KeyError`. Using `my_dict.pop(key, None)` will safely remove a key if it exists but won't crash if it doesn't. This is a great habit for writing robust code.

### 3. Dictionary Comprehensions are the Key to Filtering

This was the biggest pattern I learned. For creating a new dictionary from an old one based on a condition, the dictionary comprehension is the best tool.

-   **The Pattern:** `{key: value for key, value in my_dict.items() if condition}`
-   **Example (values below a number):** `{k: v for k, v in my_dict.items() if v < 5}`
-   **Example (keys starting with a letter):** `{k: v for k, v in my_dict.items() if k.startswith('c')}`

### 4. How to Loop Properly

I made a few mistakes with loops. I learned the best way to get the data I need is by using the right method:
-   `.keys()` to loop over just the keys.
-   `.values()` to loop over just the values.
-   `.items()` to loop over both the key and value at the same time. This is the one I'll use most often in loops and comprehensions.

### 5. Modifying a Dictionary vs. Creating a New One

This was a more advanced concept. I learned the difference between:
-   **Modifying (Mutation):** Operations like `my_dict[key] = value` or `my_dict.pop(key)` change the original dictionary.
-   **Creating a Copy:** A dictionary comprehension, or using `{**my_dict, new_key: new_value}`, creates a brand new dictionary and leaves the original untouched.

---

## New Habits to Build

-   **Dictionary Comprehensions First:** For any kind of filtering, this should be my go-to method.
-   **Use `.items()`:** For loops and comprehensions, `.items()` gives me everything I need.
-   **Be Safe:** Use `.pop(key, default)` to avoid errors when removing keys.
-   **Be Intentional:** Decide if I want to modify the original dictionary or create a new one.

I feel like I have a much better handle on dictionaries now. The comprehension syntax, in particular, seems really powerful.