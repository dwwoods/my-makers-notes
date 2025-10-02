# My Reflections on the Python Drills

I've just finished working through a set of Python function drills and wanted to write down my thoughts on what I learned, especially the concepts that I found challenging at first.

## Key Concept 1: The Anatomy of a Function

The first thing I struggled with was the basic syntax for defining a function. When I tried the say_hello_to function, my first attempt was:

Python

def say_hello_to("name1"):

My key takeaway was that the item in the parentheses, the parameter, is a placeholder variable, not a fixed string. I learned to think of it as a label for the data that will be passed in later. That's why I needed to remove the quotes. I now understand the correct syntax is:

Python

def say_hello_to(name1):
    return f'Hello, {name1}!'

i.e. 'name1' is a variable that will hold whatever value I pass in.

## Key Concept 2: Crafting Conditional Logic (and vs. or)

Both_odd After a few tries, I got it to work with the following code:

Python

def both_odd(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return False
    if num1 % 2 == 0 or num2 % 2 == 0:
        return False
    else:
        return True

This worked because I systematically eliminated all the cases that should be False. However, I realized that my second if statement using or actually made the first if statement redundant. This taught me a valuable lesson about the difference between and and or, and how to simplify my logic.

## Key Concept 3: Simplifying to a Single Boolean Return

This was probably the biggest "aha!" moment for me. When I wrote my one_even function, it looked like this:

Python

def one_even(num1, num2):
    if num1 % 2 == 0 or num2 % 2 == 0:
        return True
    else:
        return False

This is perfectly correct, but I discovered a more concise way to write it. The expression num1 % 2 == 0 or num2 % 2 == 0 is a Boolean expression, which means it evaluates to True or False all by itself.

So, I learned that the entire if/else block can be simplified to a single line:

Python

def one_even(num1, num2):
    return num1 % 2 == 0 or num2 % 2 == 0

The expression itself is either True or False, so I can just return it directly!
I realized I could apply this pattern to many of the other exercises. It also helped me find a bug in my divisible_by_three function. I had written number % 3 <= 1, but I now know the remainder must be exactly 0. Using this new, simpler pattern, the fix is much cleaner:

Python

def divisible_by_three(number):
    return number % 3 == 0

Overall I feel like I've moved from just getting the code to work through a fight to sometimes getting it first try. 