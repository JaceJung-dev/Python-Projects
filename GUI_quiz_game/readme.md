# GUI Quiz Game Application

## What I learned
- How to unescape HTML entities.
- How to use Class-based structure with tkinter.

## Code Example in Action
- Text may contain HTML entities such as `&quot;`, `&amp;`, or `&#039;`. 
- To display these correctly in the GUI, we need to unescape them into human-readable characters.

```python
import html

raw_text = "What is the name of the &quot;main character&quot; in the book?"
clean_text = html.unescape(raw_text)

print(raw_text)
print(clean_text)
```

```
What is the name of the &quot;main character&quot; in the book?
What is the name of the "main character" in the book?
```