# The Golden Square

*Started: 13 Oct 2025*


This module is Golden Square Practices - 

## Learning Objectives - 

Learn to test-drive programs with multiple classes.
Learn to break programs up into classes.
Learn to debug your programs.
Learn to build software as a pair.
Learn to explain why test-driving, object-oriented design, debugging, and pairing are powerful practices for software engineers. The Golden Square refers to four software engineering practices:

## The Golden Square is: 

    • Test-Driving (TDD)
    • Object-Oriented Design (OOD)
    • Debugging
    • Pairing

## Test-Driving (TDD)
Test-driving is a software development practice where developers write tests before writing the actual code. This ensures that the code is working as expected and helps to prevent bugs.

*   **Write a failing test:** Start by writing a test for a small, specific piece of functionality you want to add. For instance, in a debugging tool, you might write a test to check if a `Debugger` class can identify a "syntax error".
*   **Make the test pass:** Write the simplest possible code to make the test pass. This might involve creating the `Debugger` class and a basic method that returns "syntax error".
*   **Refactor:** Improve the code's structure and clarity without changing its behavior. For example, you could move the error-checking logic into a separate, more specialized function.

### Object-Oriented Design (OOD)
Object-oriented design is a programming paradigm that is based on the concept of objects. Objects are data structures that contain both data and methods. This helps to organize code and make it more reusable.

*   **Identify Classes and Objects:** Think about the different parts of your program as objects. In our debugging example, you might have a `CodeFile` object to hold the source code, a `BugDetector` object to find errors, and a `Report` object to present the findings.
*   **Define Responsibilities:** Each class should have a clear, single responsibility. The `CodeFile` class is responsible for reading and providing access to the code. The `BugDetector` is responsible for analyzing the code for errors. The `Report` class is responsible for formatting and displaying the results.
*   **Establish Collaborations:** Determine how objects will interact. The main program might create a `CodeFile` object, pass it to a `BugDetector` object, and then use a `Report` object to show the `BugDetector`'s findings.

### Debugging
Debugging is the process of finding and fixing errors in code. This is an essential skill for all programmers.

*   **`pytest` for focused testing:** Use `pytest` to run specific tests or test files. This helps you to isolate the bug and test the fix without running the entire test suite. You can also use `pytest` with the `-k` flag to run tests with names that match a given string expression.
*   **`print()` statements for inspecting variables:**  Strategically place `print()` statements in your code to output the values of variables at different points in your program's execution. This can help you trace the flow of data and identify where things go wrong.
*   **Rubber ducking for explaining the problem:**  Explain your code and the problem you're facing to someone else, or even to an inanimate object like a rubber duck. The act of verbalizing your thought process can often help you spot the flaw in your logic.
*   **Read error messages carefully:** Error messages and stack traces provide valuable clues about what went wrong. Don't just skim them. Read them carefully to understand the type of error, where it occurred, and the sequence of calls that led to it.

### Pairing
Pairing is a software development practice where two programmers work together on the same code. This helps to improve code quality and knowledge sharing.

*   **Driver-Navigator:** One person (the "driver") writes the code, while the other (the "navigator") reviews it, suggests improvements, and keeps an eye on the overall direction.
*   **Ping-Pong:** One developer writes a failing test, and the other writes the code to make it pass. They then switch roles for the next test.
*   **Knowledge Sharing:** Pairing is a great way to spread knowledge and skills throughout the team.
*   **Improved Code Quality:** Having two sets of eyes on the code leads to fewer bugs and better-designed solutions.

## Object Oriented Programming

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data, in the form of fields (often known as attributes or properties), and code, in the form of procedures (often known as methods). A key feature of objects is that an object's own procedures can access and often modify its own data fields.

The main principles of OOP are `encapsulation`, `inheritance`, and `polymorphism`. 

    Encapsulation is the bundling of data with the methods that operate on that data. 
    Inheritance is a mechanism where a new class inherits properties and behavior from an existing class. 
    Polymorphism allows objects of different classes to be treated as objects of a common super class.

OOP is important because it helps to create modular and reusable code. By organizing code into objects, it becomes easier to manage and maintain complex software systems. It also promotes code reuse through inheritance, which can save time and effort in development. The modular nature of OOP also makes it easier to debug and test code, as you can isolate and test individual objects.

### Benefits of Using These Practices
Adopting these practices leads to higher quality software. Test-driving reduces bugs and regressions. Object-oriented design leads to more maintainable and scalable code. Effective debugging skills reduce the time it takes to fix issues. Pairing improves team collaboration, knowledge sharing, and code quality. Together, they form a powerful framework for building robust and reliable software.
