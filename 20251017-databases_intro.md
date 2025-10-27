# Databases & SQL Module Introduction

This module introduces the fundamentals of relational databases and the Structured Query Language (SQL). We will cover how to interact with databases from within a program, design database schemas, and represent data relationships effectively.

## Module Scope & Environment

For this module, all database work will be performed locally on your development machine (Mac). We will focus on setting up and interacting with a local database instance. Concepts related to remote databases, servers, and deployment will be covered in later modules.

## Learning Objectives

By the end of this module, you will be able to:

* **Use SQL to query a database to read data from one table or resulting of a join, create new records, update and delete.**
  * This involves mastering the basic CRUD (Create, Read, Update, Delete) operations using SQL commands like `INSERT`, `SELECT`, `UPDATE`, and `DELETE`. You'll learn to fetch data from single tables and combine data from multiple tables using `JOIN`.

* **Integrate a relational database with a program by test-driving classes which implement CRUD methods to send SQL queries to a database.**
  * You will apply your programming skills to build a bridge between your application and the database. This includes writing code that executes SQL queries to manage data, all guided by a test-driven development (TDD) approach to ensure your code is reliable and works as expected.

* **Explain how your program communicates with the database by creating a sequence diagram.**
  * Visualizing the flow of information is key. You will learn to create sequence diagrams to map out the step-by-step interactions between your application's objects and the database, making the communication process clear and understandable.

* **Design a database schema with at least two tables from a specification, including a one-to-many relationship between two tables, and create the schema in a database using SQL.**
  * This objective focuses on database design. You'll take a set of requirements and translate them into a logical database structure (schema). This includes defining tables, columns, and establishing relationships between them, such as the common "one-to-many" relationship (e.g., one author can have many books). You will then implement this schema using SQL's Data Definition Language (DDL).

## Personal Goals for this Module

Based on my ongoing development, here are some personal goals to focus on during this module:

* **Connect Technical Skills with Communication:** When explaining how my program communicates with the database (e.g., when creating a sequence diagram), focus on making the explanation clear and empathetic to the audience. Practice breaking down complex technical topics in a way that is easy for others to understand.

* **Embrace the Learning Process with Learner Safety:** This is a new and complex topic. I will embrace "Learner Safety" by giving myself permission to ask questions, experiment, and make mistakes. When I don't understand something, I will see it as an opportunity for growth rather than a failure.

* **Practice Proactive Feedback:** When pairing on database challenges, I will actively use the `AASK` model (Ask, Actionable, Specific, Kind) to give and receive feedback. I will also be proactive in seeking feedback on my SQL queries and database designs to identify my blind spots early.

* **Reinforce Tooling Habits:** Continue to solidify the habit of using Git for all projects. I will focus on making small, atomic commits with clear, descriptive messages that tell a story of the development process, especially when building and modifying the database schema and application code.

## Key Technologies

This module will focus on the following specific technologies:

* **Database System:** **PostgreSQL** (often shortened to "Postgres"), a powerful, open-source object-relational database system.
* **Query Language:** **SQL** (Structured Query Language), the standard language for managing and manipulating relational databases.
* **Python Interface:** The **`psycopg`** library, the most popular PostgreSQL database adapter for the Python programming language. It allows our Python programs to connect to and communicate with a PostgreSQL database.

## What are CRUD Methods?

**CRUD** is an acronym that stands for the four fundamental functions of persistent storage: **C**reate, **R**ead, **U**pdate, and **D**elete. These operations are the building blocks for most applications that manage data.

When we talk about "CRUD methods" in the context of programming, we are referring to the functions or methods in our application code that execute these four operations against a database.

Here's how they map to SQL commands:

* **Create**: Adds new data to the database.
  * **SQL Command:** `INSERT`
* **Read**: Retrieves or queries data from the database.
  * **SQL Command:** `SELECT`
* **Update**: Modifies existing data in the database.
  * **SQL Command:** `UPDATE`
* **Delete**: Removes data from the database.
  * **SQL Command:** `DELETE`

## Understanding Table Relationships

In a relational database, data is organized into tables. The real power comes from linking these tables together through relationships. These relationships model real-world connections and help prevent data duplication.

The key to creating these relationships is the **foreign key**. A foreign key is a column in one table that refers to the primary key of another table, creating a link between them.

There are three main types of relationships:

### One-to-Many (1:N)

This is the most common relationship type. It means one record in a table can be associated with many records in another table, but each record in the second table is associated with only one record in the first.

* **Example:** An `authors` table and a `books` table.
  * One author can write **many** books.
  * Each book is written by only **one** author.
* **Implementation:** The `books` table would contain a foreign key column (e.g., `author_id`) that stores the `id` of the corresponding author from the `authors` table.

### One-to-One (1:1)

This relationship exists when one record in a table is associated with exactly one record in another table. This is often used to split a large table into smaller parts or for security purposes.

* **Example:** A `users` table and a `user_profiles` table.
  * Each user has **one** profile.
  * Each profile belongs to only **one** user.
* **Implementation:** The `user_profiles` table would have a foreign key `user_id` that is also set as a unique key, ensuring no two profiles can link to the same user.

### Many-to-Many (M:N)

This relationship occurs when multiple records in one table can be associated with multiple records in another table.

* **Example:** A `students` table and a `courses` table.
  * One student can enroll in **many** courses.
  * One course can have **many** students.
* **Implementation:** You cannot link these tables directly. Instead, you use a third table, often called a **join table** or **junction table**. This table holds foreign keys to both tables, creating two one-to-many relationships.
  * The `students_courses` join table would have a `student_id` and a `course_id`.
  * This creates a one-to-many relationship between `students` and `students_courses`.
  * It also creates a one-to-many relationship between `courses` and `students_courses`.

    **Example Join Table (`students_courses`):**

```
    +-------------+------------+
    | student_id  | course_id  |
    +-------------+------------+
    | 1           | 101        |  -- Student 1 is in Course 101
    | 1           | 102        |  -- Student 1 is also in Course 102
    | 2           | 101        |  -- Student 2 is in Course 101
    +-------------+------------+
```
