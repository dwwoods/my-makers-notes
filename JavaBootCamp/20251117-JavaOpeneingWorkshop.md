# My First Java Lesson Notes

## My Objectives for this Module

1. **Master the Fundamentals:** I want to build a solid understanding of Java's core concepts, including what Object-Oriented Programming is, how the JVM works, and the difference between the JDK and JRE.
2. **Become Self-Sufficient:** My goal is to be able to write, compile, and run my own simple Java applications without needing step-by-step guidance.
3. **Learn the Syntax:** I will focus on getting comfortable with the basic building blocks of the language: declaring variables with the correct data types, writing methods, and using control flow statements like `if` and `for`.

## The TOs are for this modlue 

1. **Apply a coherent process to learn a new language.**
2. **Test-drive simple programming problems using Java.**

## What is Java?

Today I learned about Java. It's a high-level, **object-oriented**, **statically-typed**, and **compiled** programming language.

One of the coolest things about it is that it's designed to be "platform-independent." This means I can write my code once on my computer (a Mac, for instance) and it can run on other systems like Windows or Linux without me having to change it. This principle is called "Write Once, Run Anywhere" (WORA).

It's used for a lot of different things, including web servers, application and cloud development, and building Android mobile apps.

## Key Terminology: The Three-Letter Acronyms

I need to get these straight, as they seem very important.

* **JVM (Java Virtual Machine):** This is like a mini-computer running inside my actual computer. When I run a Java program, it's the JVM that actually executes the code. Each operating system (Windows, Mac, Linux) has its own specific JVM, and this is the magic that makes Java platform-independent. My code runs on the JVM, not the OS directly.

* **JRE (Java Runtime Environment):** This is the software package that contains everything needed to *run* a Java application. It includes the JVM and a set of standard libraries (core classes) that my programs can use. If I just want to run a Java program someone else wrote, I only need the JRE.

* **JDK (Java Development Kit):** This is the package for *developing* Java applications. It includes everything the JRE has, plus tools for programming, like the compiler (`javac`). Since I want to write my own code, this is what I needed to install.

**In short:** I use the **JDK** to write code, which creates a program that runs on the **JRE**, which uses the **JVM** to execute it on my machine.

## Diving Deeper: Core Concepts

I need to remember these fundamental ideas about how Java works.

* **Object-Oriented Programming (OOP):** The instructor said "everything in Java is a class or an object." This means the language is built around the idea of "objects." I can think of an object as a self-contained component that models a real-world thing, like a `User` or a `Car`. Each object has its own data (properties) and behaviors (methods). The "blueprint" used to create these objects is called a **class**. My `HelloWorld` program was a simple example of a class.

* **Compiled Language:** Java is a compiled language, which means my human-readable `.java` file is translated into a computer-readable format before it can be run. This is different from an *interpreted* language (like Python or JavaScript) where code is read and executed line-by-line.
  * The interesting part is that Java is compiled into an intermediate language called **bytecode** (the `.class` file). This bytecode isn't tied to a specific OS; instead, it's run by the JVM, which then translates it for the specific machine. This is how "Write Once, Run Anywhere" is achieved.

* **Statically Typed:** I learned that Java is "statically typed." This means I must declare the type of every variable I create. For example, I have to tell Java whether a variable will hold a whole number (`int`), a decimal number (`double`), or text (`String`).

* **Encapsulation (and Access Modifiers):** This is another core pillar of OOP. Encapsulation means bundling the data (fields) and the methods that operate on that data together within a single unit (a class). It also involves hiding the internal state of an object from the outside world.

    Think of a car. You, the driver, interact with a simple interface: a steering wheel, pedals, and a gear stick. You don't need to know how the engine, transmission, or electronics work internally. The car's internal complexity is **encapsulated**.

    In Java, we achieve this using **access modifiers** like `public` and `private`.

    *   `private`: When a field or method is `private`, it can only be accessed from *inside* the same class. This is the default choice for an object's data (its fields) to protect it from accidental outside modification.

    *   `public`: When a field or method is `public`, it can be accessed from *anywhere*—from other classes in your project, or even from other programs. This is used for the "public interface" of your class, like the car's steering wheel.

    Here's a simple example of a `User` class that demonstrates encapsulation:

    ```java
    public class User {
        private String username; // Private: cannot be accessed directly from outside

        // Public "getter" method to safely expose the username
        public String getUsername() {
            return this.username;
        }

        // Public "setter" method to allow controlled updates
        public void setUsername(String newUsername) {
            this.username = newUsername;
        }
    }
    ```

    By making `username` private, we force other parts of the code to use the `getUsername()` and `setUsername()` methods. This gives us control over how the data is read and changed.

    ```java
    int myAge = 30; // I must declare this is an integer.
    String myName = "David"; // I must declare this is a String.
    ```

    The Java compiler checks all these types *before* I run the program. If I try to put text into a number variable, it will give me an error. This seems really useful for catching bugs early on, before the program even starts.

## My First Java Program: "Hello, World!"

I wrote my first program! The tradition is to make it print "Hello, World!" to the screen.

Here's the code I wrote. It has to be saved in a file named `HelloWorld.java`. The file name must exactly match the `public class` name.

```java
public class HelloWorld {
    // This is the main method, the entry point of the program.
    public static void main(String[] args) {
        // This line prints "Hello, World!" to the console.
        System.out.println("Hello, World!");
    }
}
```

### Breaking Down the Code

I need to understand what each part does.

* `public class HelloWorld { ... }`
  * This defines a **class** named `HelloWorld`. In Java, all code lives inside classes. This is the main container for my program.

* `public static void main(String[] args) { ... }`
  * This is the **main method**. When I run the program, the JVM looks for this exact method to start execution. It's the entry point.
  * `public`: The method can be called from anywhere.
  * `static`: The method belongs to the `HelloWorld` class itself, not an instance of it. This means the JVM can run it without creating a `HelloWorld` object first.
  * `void`: The method doesn't return any value.
  * `main`: This is the name of the method.
  * `(String[] args)`: This is a parameter for command-line arguments. I can pass information into my program when I run it. For now, I'm not using it, but it has to be there.

* `System.out.println("Hello, World!");`
  * This is the statement that does the work.
  * `System`: A built-in Java class that contains useful tools.
  * `out`: An object within the `System` class that handles output.
  * `println()`: A method that prints a line of text to the console. The text I want to print goes inside the parentheses and quotes.
  * The semicolon `;` at the end is important. It marks the end of a statement in Java, like a period in a sentence.

## How I Compiled and Ran My Program

Writing the code is only the first step. I then had to turn it into something the computer can run.

1. **Save:** I saved the code above into a file named `HelloWorld.java`.

2. **Compile:** I opened my terminal, navigated to the directory where I saved the file, and ran the Java compiler:

    ```sh
    javac HelloWorld.java
    ```

    This didn't print anything, but it created a new file in the same folder: `HelloWorld.class`. This file contains **bytecode**, which is the language the JVM understands.

3. **Run:** With the `.class` file created, I could now run my program using the `java` command. I don't include the `.class` extension here.

    ```sh
    java HelloWorld
    ```

The output in my terminal was:

```
Hello, World!
```

Success!
