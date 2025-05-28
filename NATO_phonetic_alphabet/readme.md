# List Comprehension and NATO Phonetic Alphabet

## What I learn
- How to simplify list creation using Python’s list comprehension
- How to build dictionaries effectively with dictionary comprehension
- How to loop through data in a Pandas DataFrame

## Code Example in Action
Sample data:
```python
import pandas as pd

student_dict = {
    "student": ["Andy", "Jace", "Lily"], 
    "score": [56, 100, 98]
}

student_data_frame = pd.DataFrame(student_dict)
```
Looping through dictionaries:
```python
for (key, value) in student_dict.items():
    print(f"key: {key}, value: {value}")
```
```
key: student, value: ['Angela', 'James', 'Lily']
key: score, value: [56, 76, 98]
```
Loop through rows of a data frame
Access index and row:
```python
for (index, row) in student_data_frame.iterrows():
    print(f"index >> {index}")
    print(f"row >> \n{row}")
    print("-" * 25)
```
```
index >> 0
row >> 
student    Angela
score          56
Name: 0, dtype: object
-------------------------
index >> 1
row >> 
student    James
score         76
Name: 1, dtype: object
-------------------------
index >> 2
row >> 
student    Lily
score        98
Name: 2, dtype: object
-------------------------
```
Access row.student or row.score:
```python
for (index, row) in student_data_frame.iterrows():
    print(f"row.student >> {row.student}")
    print(f"row.score >> {row.score}")
```
```
row.student >> Angela
row.score >> 56
row.student >> James
row.score >> 76
row.student >> Lily
row.score >> 98
```