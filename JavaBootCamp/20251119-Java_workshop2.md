# Multi-Class Programs: Parent Classes vs. Interfaces

When building programs with multiple classes, we need ways for them to relate to each other. Two primary mechanisms for this in Java are **inheritance** (using parent classes) and **abstraction** (using interfaces). They solve different problems but are often used together.

## Parent Class (Superclass) and Inheritance

A parent class (or *superclass*) is used to establish an **"is-a"** relationship. You use inheritance when a new class is a more specific version of an existing class. The new class (the *subclass* or child class) inherits fields and methods from the parent.

* **Keyword:** `extends`
* **Core Idea:** Code reuse and creating a hierarchy of related classes.
* **Rule:** A class can only `extend` **one** parent class. This is called single inheritance.

### Example: Animal, Cat, and Dog

A `Cat` **is an** `Animal`, and a `Dog` **is an** `Animal`. It makes sense for them to inherit common properties from an `Animal` class.

**Parent Class (`Animal.java`):**

```java
public class Animal {
    protected String name; // 'protected' is accessible by subclasses

    public Animal(String name) {
        this.name = name;
    }

    public void eat() {
        System.out.println(name + " is eating.");
    }

    public String getName() {
        return name;
    }
}
```

**Child Class (`Car.java`):**

```java
public class Car extends Vehicle {
    private int numberOfDoors;

    public Car(String brand, int numberOfDoors) {
        super(brand); // Calls the parent class's constructor
        this.numberOfDoors = numberOfDoors;
    }

    // The honk() and getBrand() methods are automatically inherited!
}
```

The `Car` class automatically gets the `brand` field and the `honk()` method from `Vehicle` without having to redefine them.

## Interface

An interface is a contract that defines a **"can-do"** relationship. It specifies a set of methods that a class *must* implement, but it doesn't provide the implementation for those methods. It's a blueprint for behavior.

* **Keyword:** `implements`
* **Core Idea:** Defining a standard set of capabilities that unrelated classes can share.
* **Rule:** A class can `implement` **multiple** interfaces.

### Example: Drivable

Many different things "can be" driven, like a car, a truck, or even a remote-controlled robot. They don't share a common parent, but they do share a capability.

**Interface (`Drivable.java`):**

```java
public interface Drivable {
    void startEngine(); // Method signatures with no body
    void drive(int distance);
    void stop();
}
```

**Implementing Class (`Car.java`):**
A `Car` **can be** driven.

```java
// Now let's make our Car implement the Drivable interface
public class Car extends Vehicle implements Drivable {
    private int numberOfDoors;

    public Car(String brand, int numberOfDoors) {
        super(brand);
        this.numberOfDoors = numberOfDoors;
    }

    // The class MUST provide an implementation for all methods in Drivable
    @Override
    public void startEngine() {
        System.out.println("Engine started.");
    }

    @Override
    public void drive(int distance) {
        System.out.println("Driving for " + distance + " miles.");
    }

    @Override
    public void stop() {
        System.out.println("Car stopped.");
    }
}
```

Notice how our `Car` class now both `extends Vehicle` and `implements Drivable`. It gets its core identity from `Vehicle` and its driving capability from `Drivable`.

## Key Differences: Parent Class vs. Interface

| Feature             | Parent Class (Inheritance)                               | Interface                                                |
| ------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| **Relationship**    | **"is-a"** (A `Car` is a `Vehicle`)                      | **"can-do"** (A `Car` can be `Drivable`)                   |
| **Keyword**         | `extends`                                                | `implements`                                             |
| **Number Allowed**  | Can extend only **one** class.                           | Can implement **multiple** interfaces.                   |
| **Content**         | Can contain fields, constructors, and implemented methods. | Primarily contains abstract method signatures (a contract). |
| **Purpose**         | Share common code and state between related classes.     | Define a common behavior for potentially unrelated classes. |
| **When to Use**     | When you have a clear class hierarchy and want to reuse implementation. | When you want to define a role or capability that different classes can perform. |

### Summary

* Use **inheritance (`extends`)** for objects that are clear, direct specializations of another object. Think of it as a family tree.
* Use an **interface (`implements`)** to define a "hat" that a class can wear. Many different classes can wear the "Drivable" hat, even if they are otherwise unrelated.

## A Note on Collections: The ArrayList

While basic arrays (like `String[] args`) are useful, they have a fixed size that you must define when you create them. What if I don't know how many items I need to store?

This is where the `ArrayList` comes in. It's a resizable array from Java's Collections Framework.

*   **Dynamic Size:** It can grow and shrink as I add or remove elements.
*   **Stores Objects:** It can only store objects, not primitive types like `int`. I have to use the "wrapper" class, `Integer`.
*   **Easy to Use:** It comes with helpful methods like `.add()`, `.get()`, `.remove()`, and `.size()`.

To use it, I first need to `import` it from Java's utility library.

### Example: A List of Tasks

Here's how I could create and use an `ArrayList` to store a list of strings.

```java
import java.util.ArrayList; // Don't forget to import it!

public class TodoList {
    public static void main(String[] args) {
        // Create an ArrayList that will store String objects
        ArrayList<String> tasks = new ArrayList<>();

        // Add items to the list
        tasks.add("Learn Java basics");
        tasks.add("Write a 'Hello, World!' program");
        tasks.add("Understand ArrayLists");

        System.out.println("My first task is: " + tasks.get(0)); // Access item by index
        System.out.println("Number of tasks: " + tasks.size()); // Check the size
    }
}
```
