# Database Workshop: PostgreSQL Fundamentals

Date: *29 Oct 2025*

This document serves as a consolidated guide for the database workshop, covering PostgreSQL setup, essential SQL concepts, and practical commands for interacting with a relational database.

## 1. Introduction to Relational Databases

A relational database organizes data into tables. Each table represents a list of records (like `students` or `posts`), and each record is a row in that table.

Tables are defined by columns, which represent the attributes of each record (e.g., `name`, `release_year`). The structure of tables and their relationships is called a **schema**.

### Naming Conventions

* Table and column names are `snake_case` (lowercase, with words separated by underscores).
* Table names should be **plural** (e.g., `albums`, `artists`).

## 2. Setting Up PostgreSQL on macOS

We will use Homebrew to install and manage PostgreSQL.

### Step 1: Install PostgreSQL

Open your terminal and run the following command. This guide uses version 15, but you can use a more recent version.

```bash
# Install PostgreSQL
$ brew install postgresql@15
```

### Step 2: Configure Your PATH

To make PostgreSQL commands available from any terminal window, you need to add it to your `PATH`. Homebrew provides the exact command to run after installation. It will look similar to this:

```bash
# Add PostgreSQL to your shell's configuration file
echo 'export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc
```

After running this, open a new terminal or run `source ~/.zshrc` for the changes to take effect.

### Step 3: Start the PostgreSQL Service

This command starts the database server and configures it to run in the background automatically.

```bash
# Start the PostgreSQL service
$ brew services start postgresql@15
```

You should see a success message confirming that the service has started.

## 3. Interacting with `psql`

`psql` is the interactive command-line tool for PostgreSQL. It lets you connect to a database, execute SQL queries, and manage your database server.

### Connecting

To connect to a specific database, use the `-d` flag:

```bash
# Connect to the 'music_library' database
$ psql -d music_library
```

### Useful Meta-Commands

Meta-commands are `psql`-specific shortcuts that begin with a backslash (`\`). They do not require a semicolon.

* `\l` — List all available databases.
* `\c <database_name>` — Connect to a different database.
* `\dt` — Display all tables in the current database.
* `\d <table_name>` — Describe a specific table (show its columns and data types).
* `\i <filename.sql>` — Execute SQL commands from a file (e.g., to load a schema).
* `\?` — Get help on all meta-commands.
* `\q` — Quit the `psql` session.

## 4. Connecting Python to PostgreSQL with `DatabaseConnection`

While `psql` is great for direct interaction, our applications need to communicate with the database programmatically. In Python, we do this using a library called `psycopg`. To make this process easier and more organized, we wrap the connection logic in a `DatabaseConnection` class.

### The Role of `DatabaseConnection`

The `DatabaseConnection` class is a helper that manages the connection to our PostgreSQL database. Its main responsibilities are:

1. **Connecting:** It establishes a connection to a specific database on the server.
2. **Executing Queries:** It provides a simple method to send SQL queries to the database and fetch the results.
3. **Seeding:** It can run SQL seed files to set up a clean, predictable database state, which is essential for testing.

By using this class, we keep our database connection logic separate from our application's business logic (e.g., our `AlbumRepository` or `ArtistRepository` classes).

### How it Works

Under the hood, `DatabaseConnection` uses the `psycopg` library to do the heavy lifting. A typical implementation looks like this:

```python
# lib/database_connection.py
import psycopg

class DatabaseConnection:
    def __init__(self, db_name):
        self.connection = psycopg.connect(f"dbname={db_name}")
        self.connection.autocommit = True

    def execute(self, query, params=[]):
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
```

* The `__init__` method connects to the database when a `DatabaseConnection` object is created.
* The `execute` method takes a SQL query, runs it against the database, and returns the rows of data. This is the primary way our repositories will interact with the database.

## 5. Core SQL Concepts

### Primary and Foreign Keys

Relationships between tables are managed using keys.

* **Primary Key (PK):** A column that uniquely identifies each row in a table. It must be unique and cannot be `NULL`. The `SERIAL` data type is perfect for creating auto-incrementing integer primary keys.

    ```sql
    -- 'id' is the primary key
    CREATE TABLE artists (
      id SERIAL PRIMARY KEY,
      name text,
      genre text
    );
    ```

* **Foreign Key (FK):** A column in one table that refers to the Primary Key of another table. This creates a link and enforces *referential integrity*.

    ```sql
    -- 'artist_id' is a foreign key linking to the 'artists' table
    CREATE TABLE albums (
      id SERIAL PRIMARY KEY,
      title text,
      release_year int,
      artist_id int,
      constraint fk_artist foreign key(artist_id) references artists(id)
    );
    ```

### CRUD Operations

**CRUD** stands for the four fundamental operations for managing data.

* **C**reate: Add new records.
  * **SQL:** `INSERT INTO artists (name, genre) VALUES ('Pixies', 'Rock');`

* **R**ead: Retrieve data.
  * **SQL:** `SELECT id, title, release_year FROM albums WHERE artist_id = 1;`

* **U**pdate: Modify existing records.
  * **SQL:** `UPDATE albums SET release_year = 1989 WHERE title = 'Doolittle';`

* **D**elete: Remove records.
  * **SQL:** `DELETE FROM albums WHERE id = 12;`

### Table Relationships

The most common type of relationship is **one-to-many**.

* **Example:** One `artist` can have many `albums`.
* **Implementation:** The "many" side (`albums` table) holds a foreign key (`artist_id`) that points to the "one" side (`artists` table).

## 6. Practical Example: The Music Library

Let's apply these concepts to a `music_library` database with `artists` and `albums` tables.

### Schema Design

1. **`artists` table:**
    * `id`: `SERIAL PRIMARY KEY`
    * `name`: `text`
    * `genre`: `text`
2. **`albums` table:**
    * `id`: `SERIAL PRIMARY KEY`
    * `title`: `text`
    * `release_year`: `int`
    * `artist_id`: `int` (This will be the foreign key)

### Example Queries

Once connected to your database (`psql -d music_library`), you can run queries.

```sql
-- Find all albums by the artist 'Pixies'
-- This requires joining the two tables

SELECT
    albums.title,
    albums.release_year
FROM albums
JOIN artists ON artists.id = albums.artist_id
WHERE artists.name = 'Pixies';
```

## 6. Seeding the Database

**Seeding** is the process of populating a database with initial data. A "seed file" is a SQL script that resets the database to a clean, predictable state. This is essential for reliable testing, development, and collaboration, as it ensures everyone is working with the same starting data.

A seed file typically performs three steps:

1. `DROP` existing tables to clear old data.
2. `CREATE` the tables again to define the schema.
3. `INSERT` the initial records needed for the application or tests.

### Running a Seed File

You can run a seed file from your terminal using `psql`. This command executes the SQL script against the specified database.

```bash
# From your terminal, connect to the database and run the seed file
$ psql -d music_library -f seeds/music_library.sql
```

In our test environment, a helper function like `db_connection.seed("seeds/music_library.sql")` automates this process for you before each test run.
