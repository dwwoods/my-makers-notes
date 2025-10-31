# Module 3 Reflections: 10 Lessons in Good SQL Practice

Date: *31 Oct 2025*

This document captures my key takeaways from the database module. These are the core principles and practices I want to carry forward to write clean, effective, and maintainable SQL.

---

## 1. Plan Your Schema Before You Code

The most important lesson was the value of designing the database schema first. Thinking through the tables, columns, data types, and especially the relationships *before* writing any application code is crucial. A well-designed schema is the foundation for a solid application.

## 2. Master Primary and Foreign Keys

The real power of a relational database comes from its relationships. I've learned that a deep understanding of how Primary Keys (PKs) uniquely identify records and how Foreign Keys (FKs) link tables together is non-negotiable. This is the mechanism that ensures data integrity.

## 3. Consistent Naming Conventions are a Lifesaver

Adopting and sticking to naming conventions makes a huge difference. Using plural table names (e.g., `posts`, `users`) and `snake_case` for all table and column names makes the schema predictable and much easier to read and work with.

## 4. Uppercase SQL Keywords for Clarity

The simple habit of writing SQL keywords in `UPPERCASE` (like `SELECT`, `FROM`, `WHERE`) and table/column names in `lowercase` makes queries instantly more readable. It visually separates the SQL logic from the schema identifiers, which is incredibly helpful for debugging.

## 5. Seeding is Essential for Reliable Testing

The concept of "seeding" the database was a major breakthrough. Having a SQL script that can reset the database to a clean, predictable state is vital for writing reliable tests. It ensures that tests are repeatable and not dependent on leftover data. Interesting in the debugging workshop to discover what happens if you dont do that.

## 6. Separate Database Logic from Application Logic

Using a `DatabaseConnection` class to handle all interactions with the database is a powerful pattern. It keeps raw SQL queries and connection management out of the main application classes (like repositories), leading to a much cleaner and more organized codebase.

## 7. Every SQL Statement Ends with a Semicolon

The fundamental rule of interacting with `psql`. The client won't execute a command until it sees a semicolon. This allows for writing complex queries across multiple lines for readability though.

## 8. Use `psql` Meta-Commands to Work Faster

The backslash (`\`) commands in `psql` are powerful shortcuts. Commands like `\l` (list databases), `\dt` (display tables), and `\d table_name` (describe table) are essential for quickly inspecting the state and structure of the database without needing a GUI tool.

## 9. Understand the CRUD to SQL Mapping

Thinking in terms of CRUD (Create, Read, Update, Delete) provides a clear mental model for database operations. Knowing how these map directly to SQL commands (`INSERT`, `SELECT`, `UPDATE`, `DELETE`) helps in structuring application logic that interacts with the database.

## 10. One-to-Many is the Most Common Relationship

I learned that the one-to-many relationship is the workhorse of database design (e.g., one author has many posts). Recognizing and implementing this pattern correctly by placing the foreign key on the "many" side of the relationship is a core skill. `I need more work on one to many and foreign keys`

---

**Overall:** This module shifted my perspective from seeing data as something temporary that lives in program memory to something persistent and structured. The key is not just storing data, but modeling the relationships between data effectively.
