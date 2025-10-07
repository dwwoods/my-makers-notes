# My Python Learning Notes
*Date: 2025-10-07*

---

## Data Structures: Storing Service Credentials

I explored different ways to structure data for storing service credentials. The goal was to move from a simple dictionary to something that could hold more information, like the date a password was added.

### The Options I Considered

1.  **Option 1: Flat Dictionary**
    * Each piece of data gets its own unique key, like `'acebook_password'` and `'acebook_added'`.
    * **My takeaway:** This gets disorganized and repetitive very quickly. It's not scalable.

2.  **Option 2: Nested Dictionary**
    * Uses the service name as the top-level key. The value is another dictionary containing all related data.
    * **My takeaway:** This is highly organized and excellent for direct lookups when I know the service name. It logically groups related data.

3.  **Option 3: A List of Dictionaries**
    * A list where each item is a dictionary representing one service.
    * **My takeaway:** This is very flexible and ideal for iterating through all the services. However, finding a specific service is less efficient than the nested dictionary approach.

### My Decision
I've chosen **Option 2 (the nested dictionary)**. It's the best structure for this use case because I'll most often want to retrieve all the information for a specific service by its name.

---

## First-Class Functions

I learned a core concept in Python: functions can be passed around and treated like any other object (strings, numbers, lists). This is called having **"first-class functions"**.

This means I can:

1.  **Assign functions to new variables:**
    ```python
    def say_hello():
      print("Hello!")

    # 'greet' is now another name for the 'say_hello' function
    greet = say_hello
    greet() # Prints "Hello!"
    ```

2.  **Pass functions as arguments to other functions:** These are called **higher-order functions**.
    ```python
    def shout(text):
      return text.upper() + "!"
    
    # This function takes another function as an argument
    def express_message(formatter_func, message):
      print(formatter_func(message))

    express_message(shout, "I am excited") # Prints "I AM EXCITED!"
    ```

### Combining Functions for Flexibility

The key benefit here is **flexibility**. When a function can accept another function as an argument, I can combine them in powerful ways. Two important patterns that emerge from this are:

1.  **Function Composition:** Chaining functions together, where the output of one becomes the input of the next.
    ```python
    def add_excitement(text):
      return text + " !!!"

    def make_uppercase(text):
      return text.upper()

    # Composing them:
    final_message = make_uppercase(add_excitement("this is important"))
    # final_message is "THIS IS IMPORTANT !!!"
    ```

2.  **Decorators:** A special Python syntax (`@`) for "wrapping" one function with another to extend its behavior without modifying its code. The `@timer` syntax is just a shortcut for `some_slow_task = timer(some_slow_task)`.
    ```python
    import time

    def timer(func):
      def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"'{func.__name__}' took {end_time - start_time:.4f} seconds.")
        return result
      return wrapper

    @timer
    def some_slow_task():
      time.sleep(1)

    some_slow_task() # Will print the time it took to run.
    ```

---

## Practical Application: The Strategy Pattern

A great example showed how to use higher-order functions to calculate taxes for different regions.

```python
def calculate_tax_for_the_shire(grossPay):
    return grossPay * 0.2

def calculate_tax_for_mordor(grossPay):
    return grossPay * 0.9 + 500

def report_pay(gross_pay, calculate_tax):
    # The `calculate_tax` argument is a function
    tax = calculate_tax(gross_pay)
    net_pay = gross_pay - tax
    return f"Your gross pay was {gross_pay}, minus {tax} makes your net pay {net_pay}"

# Usage:
print(report_pay(5000.0, calculate_tax_for_the_shire))
print(report_pay(5000.0, calculate_tax_for_mordor))
```
This demonstrates the Strategy Pattern. The main function `(report_pay)` is decoupled from the specific tax logic. I can add new tax rules (strategies) without ever changing the reporting function. This avoids messy `if/elif/else` blocks and makes the code much cleaner and easier to extend.

## Weather reporter Ex

I completed an exercise to solidify these concepts. The goal was to create a generic `report_weather` function that uses a specific "preference" function to decide if the weather is "great" or "not great".

This was my final code:

```Python
def as_sun_lover(temp):
    if temp >= 25:
        return "great"
    else:
        return "not great"

def as_snow_lover(temp):
    if temp <= 0:
        return "great"
    else:
        return "not great"

def report_weather(temp, weather_preference_func):
    feeling = weather_preference_func(temp)
    return f"Today's temperature is {temp}°C. For you, that's {feeling}."

# Testing it:
print(report_weather(26, as_sun_lover))  # Output: ... For you, that's great.
print(report_weather(26, as_snow_lover)) # Output: ... For you, that's not great.

```