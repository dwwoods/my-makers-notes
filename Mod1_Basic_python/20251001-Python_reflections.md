# Python Reflections

## Beyond Strings 

Source : https://journey.makers.tech/pages/beyond-strings

In a few sentences, explain:

### What integers are and how they are different to floats

    integers (or int) are whole numbers, like -5, 0, or 100. They don't have any decimal points. Floats are numbers that do have a decimal point, even if the part after the decimal is zero, such as 3.14 or 99.0. The main difference is that floats can represent fractional numbers, while integers cannot.

        Integer example: x = 10

        Float example: y = 10.5


### What Booleans are plus how the and, or and not logical operators work

    A Boolean (or bool) is a data type that can only have one of two values: True or False. Think of it as a simple switch that can only be on or off. Booleans are used to control the flow of a program based on whether a condition is met. They take the same rules as + & - in maths i.e:

        and: Returns True only if both of the conditions you're comparing are True.

            True and True is True

            True and False is False

        or: Returns True if at least one of the conditions is True.

            True or False is True

            False or False is False

        not: Simply reverses the value.

            not True becomes False

            not False becomes True

## Conditionals if, elif, and else

In a few sentences, explain:

### What is meant by conditional
    Conditional logic is all about making decisions. It lets you run specific blocks of code only when certain conditions are True.

### How the if and elif branches of an if statement work
    The if statement starts the check. If its condition is True, its code block runs, and the entire if/elif/else structure is skipped.

    elif (short for "else if") lets you check another condition if the first if statement was False. You can have as many elif statements as you need.

### How the else branch of an if statement works
    The else statement is a catch-all at the end. Its code runs only if all the preceding if and elif conditions were False.
        
### What each of these comparison operators do: ==, !=, >, >=, <, <=
    hese operators are used inside conditional statements to compare two values. They always result in a Boolean value (True or False).

        == : Is equal to (e.g., x == 10)

        != : Is not equal to (e.g., x != 10)

        > : Is greater than (e.g., x > 10)

        >= : Is greater than or equal to (e.g., x >= 10)

        < : Is less than (e.g., x < 10)

        <= : Is less than or equal to (e.g., x <= 10)

### What this operator does: % - The modulo operator 
    Doesn't do normal division. Instead, it gives you the remainder of a division. It's very useful for checking if a number is even or odd.

    10 % 3 results in 1 (because 10 divided by 3 is 3 with a remainder of 1).

    10 % 2 results in 0 (because 10 divides evenly by 2, leaving no remainder).

## Loops for & while

### What is a Loop  
    A loop is a control structure that repeats a block of code multiple times. Instead of writing the same instruction over and over, you can use a loop to automate repetitive tasks. 

### for vs while
    The main difference between for and while loops is how they decide to stop.

        A for loop is used when you know how many times you want to iterate. It runs for each item in a given sequence, such as a list or a range of numbers. You would use it to process every character in a string or every number in a list.

        A while loop is used when you want to repeat a task as long as a certain condition remains True. You would use it when you don't know the exact number of iterations in advance, like waiting for user input or running until a specific goal is met.

### Escaping an Infinite Loop
    force it to stop by pressing Ctrl+C in your terminal. This sends a KeyboardInterrupt signal that terminates the script.

### How to Loop from 50 to 100
    You can loop from 50 to 100 in steps of 3 using a for loop with the range() function. The range() function takes start, stop, and step arguments. Note that the stop value is exclusive, so you must use 101 to include 100.
        for number in range(50, 101, 3):
            print(number)

## Executing Python files (.py)

In a few sentences, explain:

### How to execute Python code that is written in a file
    ou use the python command in your terminal, followed by the name of the file. If your file is named my_script.py, you would run it by typing python my_script.py and pressing Enter. 

### What happens when you try to execute code from a file that doesn't exist
    python will stop immediately and raise a FileNotFoundError. The terminal will display an error message indicating that it could not find the file you specified, and no code will be run.

### The pros and cons of this new approach to code execution
    Executing code from a file is the standard way to run programs, offering significant advantages over typing code directly into an interactive session.

        Pros: This approach makes your code reusable, shareable, and organized. You can build complex applications, save your work, and run the same script multiple times without retyping. It also allows for version control and collaboration with others.

        Cons: The main drawback is a slightly slower feedback loop. Instead of getting an immediate result after each line, you must save the file and switch to the terminal to run it, which can be less convenient for quick tests or simple calculations.

## Defining functions

In a few sentences describe:

### The Benefit of Defining Functions
    The main benefit of defining your own functions is code reusability. Instead of writing the same block of code multiple times, you can define it once as a function and then call it whenever you need it. This practice, known as DRY (Don't Repeat Yourself), makes your code much cleaner, more organized, and easier to debug and update. 

### Function Syntax and Structure
    A function in Python is defined using the _def_ keyword. The structure consists of the function's name, a set of parentheses containing any parameters (inputs), and a colon to start the indented code block. The code block can also include an optional return statement to send a value back as output.

        'def' keyword starts the function definition
        'parameter1', 'parameter2' are placeholders for the inputs
                def function_name(parameter1, parameter2):
                    # The indented block of code is the function's body
                    # It performs actions using the parameters
                    result = parameter1 + parameter2
    
                The 'return' keyword sends a value back out of the function
                return result