# IntelliJ IDEA: Shortcuts and Tips

This document is for collecting useful shortcuts and productivity tips for working with Java in IntelliJ IDEA.

## Tips and Tricks in IntelliJ

IntelliJ is packed with features to speed up development. Here are some of the most impactful ones I've found.

### Live Templates (Code Snippets)

Live Templates are abbreviations that expand into common code structures. You've already found `sout`, which is a great one!

*   **`sout`**: Prints `System.out.println();`
    *   Just type `sout` and press `Tab` or `Enter`.
*   **`psvm`**: Creates the `public static void main(String[] args)` method.
    *   This is a huge time-saver for creating runnable classes.
*   **`fori`**: Creates a standard `for` loop.
    *   Type `fori`, press `Tab`, and it will generate `for (int i = 0; i < |; i++) { ... }`, placing your cursor to set the limit.
*   **`iter`**: Creates an enhanced `for-each` loop.
    *   Type `iter`, press `Tab`, and it will generate a loop to iterate over a collection.

### Multi-Cursor Editing

Multi-cursor editing is fantastic for making the same change in multiple places at once. Here are a couple of ways to do it:

1.  **Add Cursors with the Mouse:**
    *   Hold **`Option` + `Shift`** (on macOS) or **`Alt` + `Shift`** (on Windows/Linux) and click at the different locations where you want to add a cursor. You can then type in all places simultaneously.

2.  **Select Next Occurrence:**
    *   Select a piece of text (like a variable name).
    *   Press **`Ctrl` + `G`** (on macOS) or **`Alt` + `J`** (on Windows/Linux).
    *   Keep pressing it to select the next matching piece of text. A new cursor will be added at each match, allowing you to edit them all at once.
    *   To unselect the last match, use `Ctrl` + `Shift` + `G` (macOS) or `Alt` + `Shift` + `J` (Windows/Linux).

### Essential Editing Shortcuts

| Action | macOS Shortcut | Windows/Linux Shortcut | Description |
| :--- | :--- | :--- | :--- |
| **Duplicate Line/Selection** | `Cmd` + `D` | `Ctrl` + `D` | Copies the current line (or selection) and pastes it on the next line. |
| **Delete Line** | `Cmd` + `Delete` | `Ctrl` + `Y` | Deletes the current line without having to select it first. |
| **Move Line Up/Down** | `Option` + `Shift` + `↑`/`↓` | `Alt` + `Shift` + `↑`/`↓` | Moves the current line up or down. |
| **Comment/Uncomment Line** | `Cmd` + `/` | `Ctrl` + `/` | Toggles a line comment (`//`) on the current or selected lines. |
| **Reformat Code** | `Cmd` + `Option` + `L` | `Ctrl` + `Alt` + `L` | Automatically cleans up indentation and spacing for the entire file. |

### Navigation and Refactoring

| Action | macOS Shortcut | Windows/Linux Shortcut | Description |
| :--- | :--- | :--- | :--- |
| **Search Everywhere** | Double `Shift` | Double `Shift` | The master shortcut. Find any file, class, method, or action. |
| **Go to Declaration** | `Cmd` + `B` (or `Cmd`+Click) | `Ctrl` + `B` (or `Ctrl`+Click) | Jumps to where a variable, method, or class is defined. |
| **Find Usages** | `Option` + `F7` | `Alt` + `F7` | Finds all the places where a specific class, method, or variable is used. |
| **Rename** | `Shift` + `F6` | `Shift` + `F6` | Safely renames an element everywhere it's used in the project. |
| **Extract Method** | `Cmd` + `Option` + `M` | `Ctrl` + `Alt` + `M` | Turns a selected block of code into its own method. |