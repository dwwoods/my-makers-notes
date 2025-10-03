# My Learning Reflection: Python Lists

Today I spent time working on the fundamentals of Python lists. I went from the basics of creating them to some of the more complex aspects of modifying them.

---

## Key Concepts I Learned

* **List Creation & Access**: Using `[]` to create lists and an index like `my_list[0]` to access items.
* **Adding & Removing Items**: Using `.append()` to add items and `.pop()` to remove them.
* **In-Place Operations**: Understanding that methods like `.clear()`, `.reverse()`, and `.sort()` modify the original list.
* **Getting Help**: Using iPython's `?` command or the `help()` function to get more information on a method.

---

## Isues

My biggest point of confusion was understanding why some list methods seemed to return `None`. I was trying to use methods like `.clear()` to create a new, modified list, but it never worked how I expected.

For example, I wrote this, thinking `cleared_list` would become a new, empty list:

```Python
practice_list = [10, 20, 30]
cleared_list = practice_list.clear() 

print(cleared_list)
Output: None
```

It was only when I checked the original practice_list instead. I saw that it had been emptied. I now get that methods like `.clear()`, `.reverse()`, and `.sort()` are in-place operations—their job is to change the original list, not create a new one to give back.

I also had to figure out the default behaviors of some other methods. I was surprised that `.pop()` removed the last item, not the first, and that `.sort()` put capital letters at the front of the list. This taught me that I need to pay attention to a method's optional arguments. Now I know I can use .pop(0) to get the first item, or use the `key` argument in `.sort()` to get the exact behavior I want.

```Python
word_list = ["cherries", "Bananas", "apples"]
# This tells sort() to look at the lowercase version of each word for ordering
word_list.sort(key=str.lower)

print(word_list)
# Output: ['apples', 'Bananas', 'cherries']
```

## Summary
Good progress. 