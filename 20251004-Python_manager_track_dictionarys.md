# My Python Learning Notes: Dictionaries

These are my notes from a learning session focused on Python dictionaries. The goal was to understand their structure and learn how to use their most common methods.

-----

## Key Concepts & Breakthroughs

A few key ideas really clicked for me during this session.

1.  **Core Idea: Key-Value Pairs**: The main concept I've grasped is that dictionaries are all about **`key: value`** pairs. It's just like a real dictionary: you use a unique **key** (a word) to look up its associated **value** (the definition).

2.  **My Sticking Point - Key Types**: I initially thought dictionary keys could only be strings. I struggled with this idea for a bit. The breakthrough was realizing the rule isn't about the data type, but about **immutability**. The key just has to be something that can't be changed in place (like numbers, strings, or tuples), which is why a list can't be a key.

3.  **The Game-Changer Moment - Tab Completion**: The biggest "aha\!" moment was discovering that I can type the name of a dictionary variable, add a dot (`.`), and hit the `Tab` key to see a list of all its available methods. This is a massive shortcut for me, as it means I can **explore** what's possible instead of trying to memorize everything.

-----

## Dictionary Method Examples

Here are the practical examples of the methods I worked through.

### `.keys()`

This method returns all the keys from the dictionary.

```python
# The dictionary I used for practice
practice_dict = {
    'London': 'England', 
    'Edinburgh': 'Scotland', 
    'Cardiff': 'Wales', 
    'Belfast': 'Northern Ireland'
}

# Get all the keys
print(practice_dict.keys())
# Output: dict_keys(['London', 'Edinburgh', 'Cardiff', 'Belfast'])
```

### `.values()`

This returns all the values from the dictionary.

```python
# The dictionary I used for practice
practice_dict = {
    'London': 'England', 
    'Edinburgh': 'Scotland', 
    'Cardiff': 'Wales', 
    'Belfast': 'Northern Ireland'
}

# Get all the values
print(practice_dict.values())
# Output: dict_values(['England', 'Scotland', 'Wales', 'Northern Ireland'])
```

### `.items()`

This returns all the key-value pairs, structured as tuples. This seems really useful for loops.

```python
# The dictionary I used for practice
practice_dict = {
    'London': 'England', 
    'Edinburgh': 'Scotland', 
    'Cardiff': 'Wales', 
    'Belfast': 'Northern Ireland'
}

# Get all the key-value items
print(practice_dict.items())
# Output: dict_items([('London', 'England'), ('Edinburgh', 'Scotland'), ('Cardiff', 'Wales'), ('Belfast', 'Northern Ireland')])
```

### `.get(key)`

This is the "safe" way to access a value. If the key doesn't exist, it returns `None` instead of crashing with a `KeyError`, which is what happens with square bracket `[]` access.

```python
# The dictionary I used for practice
practice_dict = {
    'London': 'England', 
    'Edinburgh': 'Scotland', 
    'Cardiff': 'Wales', 
    'Belfast': 'Northern Ireland'
}

# Safely get a value for a key that does NOT exist
print(practice_dict.get('Dublin'))
# Output: None
```

### `.pop(key)`

This method **removes** a key-value pair. It also returns the value of the key that was just removed. This modifies the dictionary itself.

```python
# The dictionary I used for practice
practice_dict = {
    'London': 'England', 
    'Edinburgh': 'Scotland', 
    'Cardiff': 'Wales', 
    'Belfast': 'Northern Ireland'
}

# Remove 'Cardiff' and store its value
removed_value = practice_dict.pop('Cardiff')
print(f"Removed value: {removed_value}")
# Output: Removed value: Wales

# The dictionary is now changed
print(practice_dict)
# Output: {'London': 'England', 'Edinburgh': 'Scotland', 'Belfast': 'Northern Ireland'}
```

### `setdefault(key, default)`

This method is for getting a key's value, but with a special power: if the key doesn't exist, it will **add** it to the dictionary with the default value I provide.

```python
# The dictionary I used for practice
practice_dict = {
    'London': 'England', 
    'Edinburgh': 'Scotland', 
    'Belfast': 'Northern Ireland'
}

# Use setdefault for 'Dublin', which isn't in the dictionary
practice_dict.setdefault('Dublin', 'Ireland')

# The dictionary is now changed
print(practice_dict)
# Output: {'London': 'England', 'Edinburgh': 'Scotland', 'Belfast': 'Northern Ireland', 'Dublin': 'Ireland'}
```