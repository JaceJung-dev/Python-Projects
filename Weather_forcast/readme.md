# Weather Forcast Application

## What I learned
- How to use an API with an API key for authentication and access.
- How to manage environment variables securely and effectively.

## Code Example in Action

1. Create a `.env` file
```dotenv
# .env
API_KEY=your_actual_api_key_here
```
- Store sensitive information like API keys or passwords in a `.env` file.
- Make sure to exclude this file from version control by adding it to `.gitignore`.

2. Load Environment Variables in Python
```python
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

print(f"Your API key is: {api_key}")
```
- Use the python-dotenv library to load variables from the `.env` file and access them using os.getenv() or os.environ.