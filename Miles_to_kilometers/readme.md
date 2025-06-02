# TKinter, *args, **kwargs and Creatign GUI Programs

## What I learn
- What *args and **kwargs mean in Python function definitions
- How to pass a variable number of arguments to a function
- How to handle optional and keyworded arguments dynamically

## Code Example in Action
`*args` collects positional arguments into a tuple.
```python
def add_all(*args):
    print(f"args: {args}")
    return sum(args)

result = add_all(1, 2, 3, 4)
print(f"Result: {result}")
```
```
args: (1, 2, 3, 4)
Result: 10
```

`**kwargs` collects named arguments into a dictionary.
```python
def print_info(**kwargs):
    print(f"kwargs: {kwargs}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Jace", age=16, language="Python")
```
```
kwargs: {'name': 'Jace', 'age': 16, 'language': 'Python'}
name: Jace
age: 29
language: Python
```