# TDD Workshop Notes

    Created Date: 2025-10-14

    Facilitor: Will O'Connell

## Core Python Concepts

* **Everything in Python is an object:** This is a fundamental principle. It means that numbers, strings, functions, classes, and modules are all objects. As objects, they have associated types, attributes (data), and methods (functions). For example, you can call methods on a string object like `"hello".upper()`.

## Project Setup Checklist

A good initial project setup is crucial. Key elements include:

* **`git` repository:** Initialize version control from the start.
* **`.gitignore` file:** Crucial for keeping the repository clean. A common practice is to add the virtual environment directory (e.g., `venv/`) to it.
* **Folder Structure:** A typical simple structure includes a `lib/` directory for your main code and a `tests/` directory for your tests.
* **`__init__.py` files:** Placing an empty `__init__.py` file in your directories (`lib/`, `tests/`) tells Python to treat them as packages, which is necessary for imports to work correctly.

## TDD Principles

* **Test Naming Conventions:** Test functions must be named descriptively and follow a specific convention.
  * The function name must start with `test_`. This is how test runners like `pytest` automatically discover which functions are tests.
  * The rest of the name should clearly describe what the test is checking. For example, `test_user_is_invalid_if_email_is_missing()` is a good, descriptive name.

* **The Red-Green-Refactor Cycle:** This is the core loop of TDD.
  * **Red:** Start by writing an automated test for a new feature or improvement. Since the code doesn't exist yet, the test will fail (this is the "red" state). This step is crucial as it proves that the test is working and can actually fail.
  * **Green:** Write the simplest, most minimal code possible to make the test pass (the "green" state). The focus here is solely on passing the test, not on writing elegant or efficient code.
  * **Refactor:** Now that you have a passing test acting as a safety net, you can clean up your code. Improve its structure, remove duplication, and increase readability without changing its external behavior. Rerun the tests frequently to ensure they still pass.

* **Small, Iterative Steps:** The TDD process is intentionally granular. You write a single failing test, make the smallest possible change to make it pass, and then refactor. This cycle of "test, run, change, repeat" is very fast and is repeated for every small piece of new functionality.

* **Interpreting `AssertionError`:** When a test fails with an `AssertionError`, it means the condition you asserted (the expected outcome) was not met. This is the primary failure signal in TDD. It indicates a discrepancy between your expectation and the code's actual behavior. The cause could be:
  * A bug in the implementation code (most common).
  * An incorrect assertion in the test itself (e.g., the test expects the wrong value).
  * A misunderstanding of the feature's requirements, leading to a flawed test.

* **Forcing Generalization (Triangulation):** A key moment in TDD is when you are forced to write real logic. This often happens as follows:
    1. You make the first test pass with a simple, hardcoded return value.
    2. You write a second test with a different input and expected output.
    3. Now, the original hardcoded value cannot satisfy both tests simultaneously. This is the point where `pytest` *demands* that you replace the hardcoded value with a more generic implementation (i.e., real logic) that can handle multiple cases.
    4. As you noted, this is a critical step that is easy to miss. If you find yourself stuck, returning to this principle of adding a second, conflicting test is often the way forward.

## `if/else` vs. `try/except`

A common point of confusion is when to use an `if/else` block versus a `try/except` block. The choice depends on whether you are handling an *expected* condition or an *exceptional* one.

* **`if/else` for Expected Conditions:** Use `if/else` for flow control based on conditions you fully expect to happen. It's for making decisions and directing the logic of your program. For example, checking `if user.is_authenticated:` or `if stock_level > 0:`. These are predictable checks that are part of the normal application flow.

* **`try/except` for Exceptional Situations:** Use `try/except` to handle errors or situations that are out of the ordinary and would otherwise crash your program. You don't check for the condition in advance; you attempt an operation and then "catch" the error if it fails. This is ideal for handling things like network failures, file I/O errors (e.g., file not found), or invalid type conversions (e.g., `int('hello')`). Using `try/except` for regular logic control is generally considered an anti-pattern as it can make the code less readable and slower.

## Best Practices for Organizing Tests

A well-organized test suite is maintainable, readable, and trustworthy. Here are some established best practices for structuring your tests:

* **Parallel Structure:** Your `tests/` directory should mirror the structure of your application's source directory (e.g., `lib/`). For every file in your source code, like `lib/user_account.py`, there should be a corresponding test file, `tests/test_user_account.py`. This makes it intuitive to locate the tests for any given piece of code.

* **The "Arrange, Act, Assert" (AAA) Pattern:** Structure the body of your test functions in three distinct, commented parts. This pattern makes tests highly readable and easy to understand.
  * `# Arrange`: Set up all the necessary preconditions and inputs. This might involve creating objects, preparing mock data, or setting up a database state.
  * `# Act`: Execute the specific function or method you are testing with the arranged parameters.
  * `# Assert`: Verify that the outcome of the action is what you expected. This is where you'll have your `assert` statements.

* **Keep Tests Independent and Isolated:** Each test case should be a self-contained unit that can run on its own, in any order, without depending on the state left behind by other tests. This is critical for a reliable test suite. Avoid "daisy-chaining" tests where one test's output is the next one's input.

* **Use Fixtures for Setup and Teardown:** For setup logic that is shared across multiple tests (like creating a database connection or a complex object), use your test framework's fixture system (e.g., `@pytest.fixture`). Fixtures help reduce code duplication and manage the setup and teardown of test resources cleanly.

* **One Assertion Per Test (Ideally):** While not a strict rule, aiming for a single assertion per test is a good guideline. It ensures that each test is focused on a single, specific behavior. When a test with a single assertion fails, you know exactly which behavior is broken. If you must have multiple assertions, ensure they are all testing a single, cohesive unit of behavior.

## Test-Driving a Function: The Workflow

Test-driving a single function follows a rapid, iterative cycle. The goal is to build up the function's logic by starting with the simplest case and progressively adding tests that force you to write more generic, robust code.

### 1. Start with the Simplest Test

First, write a test for the most basic behavior you expect. This test will fail because the function doesn't even exist yet.

* **Write the test:** In a new test file (e.g., `tests/test_greet.py`), write a test for a function `greet()`.

    ```python
    # tests/test_greet.py
    from lib.greet import greet

    def test_greet_returns_hello_world():
        result = greet()
        assert result == "Hello, World!"
    ```

* **Red:** Run `pytest`. It will fail with an `ImportError`.
* **Green:** Create the file `lib/greet.py` and write the absolute minimum code to make the test pass: a hardcoded return value.

    ```python
    # lib/greet.py
    def greet():
        return "Hello, World!"
    ```

* Run `pytest` again. The test passes.

### 2. Triangulate to Force Real Logic

The hardcoded solution is a temporary step. To force a real implementation, add a second test with different inputs and expected outputs. This is called **triangulation**.

* **Write the second test:** Add a test that passes an argument and expects a personalized greeting.

    ```python
    # tests/test_greet.py
    # ...

    def test_greet_returns_hello_name_with_given_name():
        result = greet("David")
        assert result == "Hello, David!"
    ```

* **Red:** Run `pytest`. The new test fails. The function `greet()` takes 0 positional arguments but 1 was given.
* **Green:** Modify the function to accept an argument and use it. The simplest way to make *both* tests pass is often to introduce a default parameter.

    ```python
    # lib/greet.py
    def greet(name="World"):
        return f"Hello, {name}!"
    ```

* Run `pytest` again. Both tests should now pass. You have been forced to replace the hardcoded value with a generic implementation.

### 3. Test Edge Cases and Error Conditions

Once the core logic is in place, add tests for edge cases (e.g., empty strings, `None`) and invalid inputs to make your function more robust.

* **Write an error-checking test:** For example, test that the function raises a `TypeError` if it's given a number instead of a string.

    ```python
    # tests/test_greet.py
    import pytest
    # ...

    def test_greet_raises_error_if_not_a_string():
        with pytest.raises(TypeError) as e:
            greet(123)
        assert str(e.value) == "Name must be a string."
    ```

* **Red:** Run `pytest`. The test fails because no error is raised.
* **Green:** Add a type check and raise an exception in your function.

    ```python
    # lib/greet.py
    def greet(name="World"):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        return f"Hello, {name}!"
    ```

* Run `pytest` again. All tests now pass. Continue this process for any other edge cases you can think of.

## Test-Driving a Class: The Workflow

Developing a class with TDD follows a structured, iterative process that builds the class up from nothing. The key is to let the tests guide the design of your class, including its properties and methods.

### 1. Test for Existence and Instantiation

The very first step is to test that you can create an instance of the class. This might seem trivial, but it's the simplest possible behavior and a perfect starting point.

* **Write the test:** Create a test file (e.g., `tests/test_my_class.py`) and write a test that tries to import and instantiate your class.

    ```python
    # tests/test_my_class.py
    from lib.my_class import MyClass

    def test_constructs_and_can_be_instantiated():
        my_class = MyClass()
        # No assertion needed yet, the test fails if the line above errors
    ```

* **Red:** Run `pytest`. It will fail with an `ImportError` because `lib/my_class.py` (and the class itself) doesn't exist.
* **Green:** Create the file `lib/my_class.py` and define the simplest possible class to make the test pass.

    ```python
    # lib/my_class.py
    class MyClass:
        pass
    ```

* Run `pytest` again. The test now passes.

### 2. Test-Drive the Initial State (Properties)

Next, test that an object has the correct initial state immediately after it's created. This is how you drive out the `__init__` method and its properties.

* **Write the test:** Add a test that creates an object and asserts that one of its properties has the correct default value.

    ```python
    # tests/test_my_class.py
    # ... (previous test)

    def test_initial_tasks_is_empty_list():
        my_class = MyClass()
        assert my_class.tasks == []
    ```

* **Red:** Run `pytest`. The test fails with an `AttributeError` because the `.tasks` property doesn't exist.
* **Green:** Modify the class to have an `__init__` method that creates the property.

    ```python
    # lib/my_class.py
    class MyClass:
        def __init__(self):
            self.tasks = []
    ```

* Run `pytest` again. Both tests now pass.

### 3. Test-Drive Public Methods

Once the initial state is verified, start adding behavior by test-driving the class's public methods. For each method, you'll follow the Red-Green-Refactor cycle.

* **Write the test:** Add a test for a new method, like adding a task. Use the "Arrange, Act, Assert" pattern.

    ```python
    # tests/test_my_class.py
    # ...

    def test_add_task_appends_to_tasks_list():
        # Arrange
        my_class = MyClass()
        # Act
        my_class.add_task("Walk the dog")
        # Assert
        assert my_class.tasks == ["Walk the dog"]
    ```

* **Red:** Run `pytest`. It fails with an `AttributeError` because the `add_task` method doesn't exist.
* **Green:** Implement the simplest possible code to make the test pass.

    ```python
    # lib/my_class.py
    class MyClass:
        def __init__(self):
            self.tasks = []

        def add_task(self, task):
            self.tasks.append(task)
    ```

* **Refactor:** At this stage, the code is simple and clean, so no refactoring is needed. As the class grows, you would look for opportunities to improve the code's structure while keeping the tests green.

Continue this cycle for every piece of public behavior: test-drive adding multiple items, removing items, formatting items, handling edge cases, and so on. Each new test will force you to add or refine the implementation.
