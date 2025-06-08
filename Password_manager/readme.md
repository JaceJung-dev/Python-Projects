# Password Manager GUI (Pop-ups, Exceptions and JSON)

## What I learn
- How to implement Dialog Boxes and Pop-Ups in Tkinter
- Exception Handling
- Write, read and update JSON data in python

## Code Example in Action

### Error type
- FileNotFoundError
```python
with open()
```

```
FileNotFoundError: [Errno 2] No such file or directory: 'a_file.txt'
```

- KeyError
```python
a_dict = {"key": "value"}
value = a_dict["non_existent_key"]
```

```
KeyError: 'non_existent_key'
```

- IndexError
```python
fruit_list = ["Apple", "Banana", "Pear"]
fruit = fruit_list[3]
```

```
IndexError: list index out of range
```

- TypeError
```python
text = "abc"
print(text + 5)
```

```
TypeError: can only concatenate str (not "int") to str
```

### `try-except-else-finally` statement

```python
try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["non_existent_key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as e:
    print(f"The key {e} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    raise KeyError
    file.close()
    print("File was closed.")
```

### JSON
- JavaScript Object Notation
- Lightweight data format used to store and exchange data

(1) import `json` module
```python
import json
```

(2) load JSON from file
```python
with open("data.json", "r") as file:
    data = json.load(file)
```

(3) Save Python dictionary to JSON file
```python
new_data ={
    "school1": {
    "name": "Bob",
    "age": 18,
    "is_student": True
    }
}

with open("data.json", "w") as file:
    json.dump(new_data, file, indent=4)
```

(4)) Update a JSON file
```python
# 1. Read the existing data.
with open("data.json", "r") as file:
    saved_data = json.load(file)

# 2. Update the dictionary using Python's built-in dict method.
# This merges new_data into saved_data (adds or overwrites keys)
new_data ={
    "school2": {
    "name": "Kim",
    "age": 16,
    "is_student": True
    }
}

saved_data.update(new_data)

# 3. Save the updated dictionary back to the JSON file.
with open("data.json", "w") as file:
    json.dump(saved_data, file, indent=4)

```