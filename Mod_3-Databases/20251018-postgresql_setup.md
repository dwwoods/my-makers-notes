# Setting up PostgreSQL

Date: *18 Oct 2025*

## Introduction

Up to this point, our program's data has been stored in memory (e.g., as attributes, lists, objects). This data is volatile, meaning it's lost as soon as the program exits. To store data for the long term, we need a database.

This week, we'll be using **PostgreSQL**, a popular, free, and open-source relational database system used in many large-scale, professional applications.

## About Relational Databases

A database is a collection of tables. Each table stores a list of records (or "things"). For example, a blogging application might have a `posts` table and a `comments` table.

A table is structured with columns that define the attributes for each record. Each record is a row in the table.

### Example Table

Here is an example of a `students` table:

```Markdown
Table: students

 id |     name     | cohort_name
----+--------------+------------
  1 | Sarah        | April 2022
  2 | Georgia      | April 2022
  3 | David        | May 2022
  4 | Ali          | April 2022
```

### Naming Conventions

* Table and column names are always **lowercase**.
* Words are separated by underscores (`snake_case`).
* Table names are always **plural** (e.g., `students`, `posts`).

## Setup on macOS

We will install PostgreSQL using Homebrew. The version used here is `15`, but you can substitute a newer version number if required.

### 1. Install PostgreSQL

Run the following command in your terminal:

```bash
# Install postgresql.
$ brew install postgresql@15
```

### 2. Update PATH Environment Variable

After installation, Homebrew will output a command to add the PostgreSQL `bin` directory to your system's `PATH`. This allows you to run PostgreSQL commands from anywhere in your terminal. Copy and run the command it provides, which will look like this:

```bash
echo 'export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc
```

> **Note:** This command adds a line to your `.zshrc` file, which is a configuration file that runs every time you start a new terminal session. You'll need to either open a new terminal window or run `zsh` in your current one for the change to take effect.

### 3. Start the PostgreSQL Service

This command starts the PostgreSQL software and keeps it running in the background.

```bash
# Start the postgresql software in the background.
$ brew services start postgresql@15
```

You should see the following confirmation message:
`==> Successfully started \`postgresql@15\` (label: homebrew.mxcl.postgresql@15)`

If you encounter any issues during installation, it's best to ask a coach for help.
