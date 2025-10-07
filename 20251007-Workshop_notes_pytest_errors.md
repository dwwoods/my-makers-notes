# Workshop Notes: Debugging Pytest Errors

## 1. How to Read the Pytest Output

* **Add Verbosity (`-v`)**: Run `pytest -v` to see the full name of each test and its status (`PASSED` or `FAILED`), which is more informative than the default dots. Flags can be combined, e.g., `pytest -x -v` (stop on first failure and be verbose).

* **Focus on the `E` Lines**: When a test fails, the output can be long. The lines prefixed with `E` are the most important—they contain the summary of the error or assertion.

* **Trace the Error to the Source**: The traceback shows the full issue. It will point to the failing `assert` line in your test file, but crucially, it will also point to the **exact line in your source code** (e.g., `code.py`) that produced the incorrect result. This is true for both test failures and errors like `NameError`.

## 2. `AssertionError`: The "Spot the Difference" Game

An `AssertionError` means my code ran, but it produced the wrong value. Debugging is a "spot the difference" game between the "Actual" and "Expected" output.

### Common Pitfalls

* **Type Mismatches**: Be meticulous. A common error is comparing a data structure to its string representation. Pytest's diff output will show the difference, but you have to look for the quotes.
    * `{'key': 'val'}` is a dictionary.
    * `"{'key': 'val'}"` is a string.

* **`None` is a Specific Value**: If your test fails and the "Actual" result is `None`, it means your function explicitly returned `None` or completed without a `return` statement. `None` is a real value, not the same as `0`, `False`, or an empty list `[]`.

* **In-Place Methods Return `None`**: A frequent cause of getting `None` is returning the result of an in-place method. The classic example is `list.sort()`, which sorts the list but returns `None`.
    * **Wrong**: `return my_list.sort()` (returns `None`)
    * **Right**: `my_list.sort(); return my_list`
    * **Better**: `return sorted(my_list)` (returns a new sorted list)

## 3. Logic Errors Caught by Tests

Sometimes the issue isn't a single value but a flaw in your code's logic.

### The Incomplete Loop Bug

A common bug is a `for` loop that is meant to check every item in a list but exits prematurely.

* **The Bug**: Placing a `return` statement in an `else` block inside a loop will cause the function to stop and return after checking only the **first** item.
    ```python
    # BUGGY: This only checks the very first item
    for item in items:
        if item == target:
            return True
        else:
            return False # This exits the whole function immediately
    ```
* **The Fix**: De-dent the final `return` so it is **aligned with the `for` loop**. This ensures it only runs after the entire loop has been checked.
    ```python
    # CORRECT: Checks all items before returning False
    for item in items:
        if item == target:
            return True
    return False
    ```

## 4. Other Common Errors

* **`NameError`**: This means you've used a variable or function that hasn't been defined. It's almost always a **typo** or a **missing import**. The traceback will point you to the exact line where the error is.

---

## Conclusion

Pytest provides powerful tools to help you identify not just *that* your code is wrong, but precisely *why* it's wrong. By learning to read the traceback and understanding common pitfalls like type mismatches, `None` returns, and logic errors, you can spend less time being confused by failures and more time fixing them. A failing test isn't a setback—it's a guide pointing you directly to the problem.

## Next Steps & Further Learning

To improve your debugging workflow, consider exploring these techniques:

* **"Print-Line Debugging"**: The simplest form of debugging. If you're not sure how far your code gets before it fails, put a `print("I got here!")` statement in it. Move this line around to narrow down the exact point of failure.

* **Explore Pytest Fixtures**: Learn how to use fixtures (`@pytest.fixture`) to set up complex data and services for your tests. This makes tests cleaner and more reusable.

