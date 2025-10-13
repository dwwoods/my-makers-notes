# Python Reflections

## Functions 

Please pause at this point to reflect and review your learning...

In a few sentences, explain:

### What functions are
    Like a toaster - a named, reusable block of code designed to perform a single, specific task. 

### What arguments are.
    are pieces of information or data that you pass into a function when you call it. The function then uses these arguments to perform its task. For example, in print("Hello"), the string "Hello" is the argument.

### How to use a function
    To use a function, you call it by writing its name followed by parentheses ()
#### Example
    Calling the len() function with a string argument
    word_length = len("Python") 
    print(word_length) This will print 6 i.e. the number of letter in "Python"
### Why functions are useful
    They make code more organized, readable, and reusable. 
    Also means you dont have to make things from scratch

### Where to learn about Python's built-in functions
    official Python documentation. 
    https://docs.python.org/3/library/functions.html

## Methods

In a few sentences, explain:

### What methods are
    A method is a function that belongs to a specific object. You call a method on an object to perform an action related to it, and it can access the object's internal data. object.method() remembering the ()
### How to use String methods
    You use a string method by adding a dot (.) and the method name to the end of a string variable or a literal string. These methods always return a new string. 
### How method chaining works
    calling multiple methods in a single statement. Each method in the chain operates on the return value of the previous method, from left to right.
### Where to learn about Python's string methods
    Obvs official Python documentation. but its not as neat as functions 
    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

## Further Strings

In a few sentences, explain:

### What is meant by zero-indexing
    Zero-indexing means that the position of items in a sequence (like a string) is counted starting from 0, not 1. The first item is at index 0, the second is at index 1, and so on.
### How to access the first character in a string
    To access the first character in a string, you use the index 0. 
### How to access the second character in a string
    To access the second character, you use the index 1To access the second character, you use the index 1
### How to access the last character in a string
    To easily access the last character without knowing the string's length, you use negative indexing with the index -1.
### How to slice several characters from a string
    you use the syntax string[start:end]. The slice will include the character at the start index and go up to, but not include, the character at the end index.