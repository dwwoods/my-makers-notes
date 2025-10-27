# `psql` Command-Line Interface Notes

*Date: 18 Oct 2025*

`psql` is the interactive terminal for working with PostgreSQL. It allows you to type in queries interactively, issue them to PostgreSQL, and see the query results.

## Connecting to a Database

You can connect directly to a specific database when you start `psql`.

```bash
# Connect to a database named 'my_database'
$ psql -d my_database
```

If you don't specify a database, `psql` will try to connect to a database with the same name as your user account.

## Meta-Commands (Backslash Commands)

Inside `psql`, any command that starts with a backslash (`\`) is a "meta-command". These are not SQL commands; they are shortcuts specific to the `psql` client for performing administrative tasks. You do not need a semicolon at the end of these.

*   **`\l` or `\list`**
    List all available databases on the server.

*   **`\c <database_name>`**
    Connect to a different database.

*   **`\dt`**
    Display tables. This lists all the tables in the current database. Add a `+` (`\dt+`) for more details like size.

*   **`\d <table_name>`**
    Describe a table. This shows the columns, data types, and other properties of the specified table. It's very useful for understanding a table's structure.

*   **`\i <filename.sql>`**
    Execute commands from a file. This is useful for loading a pre-written schema or a set of data into your database.

    ```sql
    -- Example: Load a schema from a file
    my_database_name=# \i lib/my_schema.sql
    ```

*   **`\?`**
    Get help. This lists all available backslash commands.

*   **`\q`**
    Quit the `psql` session and return to your regular shell.

## Executing SQL Commands

To execute standard SQL, you just type the command directly into the `psql` prompt.

**Important:** All SQL statements must end with a semicolon (`;`). `psql` will not run the command until it sees a semicolon.

This allows you to write long queries across multiple lines for readability. The prompt will change from `=>` to `->` to show that you are in the middle of a command.

```sql
-- Example: Select all records from a 'students' table
my_database_name=# SELECT id, name FROM students;

-- Example: Create a new table
my_database_name=# CREATE TABLE posts (id SERIAL PRIMARY KEY, title text, content text);
CREATE TABLE

-- Example: A multi-line query
my_database_name=# SELECT
my_database_name-#     id,
my_database_name-#     title
my_database_name-# FROM
my_database_name-#     posts
my_database_name-# WHERE title = 'My First Post';
```

### Why Use Uppercase for SQL Keywords?

Using uppercase for SQL keywords is a widely adopted convention for a simple reason: **readability**.

*   **Visual Distinction:** It makes it very easy to visually separate the SQL commands (`SELECT`, `FROM`) from the names of your tables and columns (`albums`, `title`). This is especially helpful in long and complex queries.

*   **Clarity:** Before modern code editors with syntax highlighting, capitalization was the primary way to make queries easier to read and debug. The tradition has stuck because it's still very effective.
```
