# My Reflections on Python Conditionals

This document summarizes my key learning points from my Python drills session. I focused not just on getting the code to work, but on understanding the logic and learning to write clean, efficient, and "Pythonic" code.

## 1. The Importance of Order: fizz_buzz
The fizz_buzz problem was a fantastic exercise in logical thinking. My initial code correctly used the modulo operator (%) but had a subtle bug.

My first attempt checked for divisibility in the order of 3, then 5, then 15. When my input was 15, the code checked 15 % 3, found it to be true, and immediately returned "fizz", never getting a chance to check for the fizzbuzz condition.

** Specific Before General!!** 
I should always check the most specific condition first, then move to the more general ones.

Because any number divisible by 15 is automatically divisible by 3 and 5, the number % 15 check is the most specific rule. By placing it at the top of an if/elif/else chain, I ensure it's evaluated correctly before the more general rules get a chance to execute.

My Final Code:

Python

def fizz_buzz(number):
    if number % 15 == 0:
        return "fizzbuzz" 
    elif number % 3 == 0: 
        return "fizz"
    elif number % 5 == 0: 
        return "buzz"
    else:
        return number

## 2. From Correct to "Pythonic"
In the second set of drills, my code was functionally correct, but I explored ways to make it more idiomatic—that is, written in a style that experienced Python programmers would use.

My Challenges & Concepts
Readability with in and ==: In reply_to, I used greeting.__contains__("hello"). I learned that the more standard and readable way to write this is with the in operator: 'hello' in greeting. More importantly, I realized that the rules ("if the greeting is 'hello'") implied an exact match, making the equality operator (==) the correct tool.

Ternary Expressions: For simple if/else statements that just return a value, I can use Python's compact ternary expression.


### My clear, readable version
Python

if number >= 10:
    return number - 10
else:
    return number


### The compact ternary version

return number - 10 if number >= 10 else number
Using Built-in Functions: The biggest leap was in the top_up_to_100 function. While my if/else logic was perfect, the task was essentially "find the larger of two numbers." I found the most Pythonic solution is to use the built-in max() function, which is both shorter and perfectly describes my intent.

Python

def top_up_to_100(number):
    return max(100, number)

## 3. Listening to My Tools

My final reflection was one of the most important. I noticed how VS Code behaves when I make a mistake, like forgetting a colon (:) or misspelling a variable. 