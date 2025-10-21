# 0x15. API

## Description
This project introduces you to working with APIs (Application Programming Interfaces) and data manipulation in Python. You'll learn how to consume REST APIs, parse JSON data, and export information to different file formats (CSV and JSON). Understanding APIs is crucial for modern software development as they allow different applications to communicate and share data.

## Concepts
For this project, you should understand:
- **REST API fundamentals**
- **HTTP methods (GET, POST, PUT, DELETE)**
- **JSON data format**
- **CSV data format**
- **Python requests library**
- **Data serialization**
- **API authentication and endpoints**

## Background Context
Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers who manage systems. Like their predecessors, they are doing automation, but instead of using Bash, they are using more efficient programming languages like Python.

In this project, you'll access employee data via an API and organize and export it to different data structures.

This is a perfect example of a task that is not suited for Bash scripting, so let's build Python scripts!

## Learning Objectives
At the end of this project, you should be able to explain:
- What Bash scripting should not be used for
- What is an API
- What is a REST API
- What are microservices
- What is the CSV format
- What is the JSON format
- Pythonic package and module name style
- Pythonic class name style
- Pythonic variable name style
- Pythonic function name style
- Pythonic constant name style
- Significance of CapWords or CamelCase in Python

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- Libraries imported in your Python files must be organized in alphabetical order
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- You must use `get` to access to dictionary value by key (it won't throw an exception if the key doesn't exist in the dictionary)
- Your code should not be executed when imported (by using `if __name__ == "__main__":`)

## API Information

### JSONPlaceholder API
For this project, you'll be using the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) API, a free fake REST API for testing and prototyping.

**Base URL:** `https://jsonplaceholder.typicode.com`

**Endpoints used:**
- `/users` - Get all users
- `/users/<id>` - Get specific user
- `/todos` - Get all todos
- `/todos?userId=<id>` - Get todos for specific user

**Example Response:**
```json
{
  "userId": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": false
}
```

## Tasks

### 0. Gather data from an API
**File:** `0-gather_data_from_an_API.py`

Write a Python script that, using a REST API, for a given employee ID, returns information about his/her TODO list progress.

**Requirements:**
- You must use `urllib` or `requests` module
- The script must accept an integer as a parameter, which is the employee ID
- The script must display on the standard output the employee TODO list progress in this exact format:
  - First line: `Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):`
    - `EMPLOYEE_NAME`: name of the employee
    - `NUMBER_OF_DONE_TASKS`: number of completed tasks
    - `TOTAL_NUMBER_OF_TASKS`: total number of tasks
  - Second and following lines display the title of completed tasks: `TASK_TITLE` (with 1 tabulation and 1 space before)

**Usage:**
```bash
$ python3 0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
     distinctio vitae autem nihil ut molestias quo
     voluptas quo tenetur perspiciatis explicabo natus
     aliquam aut quasi
     veritatis pariatur delectus
     nemo perspiciatis repellat ut dolor blanditiis perspiciatis sit et
     repudiandae totam in est sint facere fuga
     earum doloribus ea doloremque quis
     sint sit aut vero
```

---

### 1. Export to CSV
**File:** `1-export_to_CSV.py`

Using what you did in task #0, extend your Python script to export data in the CSV format.

**Requirements:**
- Records all tasks that are owned by this employee
- Format must be: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`
- File name must be: `USER_ID.csv`

**Usage:**
```bash
$ python3 1-export_to_CSV.py 2
$ cat 2.csv
"2","Antonette","False","suscipit repellat esse quibusdam voluptatem incidunt"
"2","Antonette","True","distinctio vitae autem nihil ut molestias quo"
"2","Antonette","False","et itaque necessitatibus maxime molestiae qui quas velit"
"2","Antonette","False","adipisci non ad dicta qui amet quaerat doloribus ea"
...
```

---

### 2. Export to JSON
**File:** `2-export_to_JSON.py`

Using what you did in task #0, extend your Python script to export data in the JSON format.

**Requirements:**
- Records all tasks that are owned by this employee
- Format must be: `{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}`
- File name must be: `USER_ID.json`

**Usage:**
```bash
$ python3 2-export_to_JSON.py 2
$ cat 2.json
{"2": [{"task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": false, "username": "Antonette"}, {"task": "distinctio vitae autem nihil ut molestias quo", "completed": true, "username": "Antonette"}, ...]}
```

---

### 3. Dictionary of list of dictionaries
**File:** `3-dictionary_of_list_of_dictionaries.py`

Using what you did in task #0, extend your Python script to export data in the JSON format.

**Requirements:**
- Records all tasks from all employees
- Format must be: `{ "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}`
- File name must be: `todo_all_employees.json`

**Usage:**
```bash
$ python3 3-dictionary_of_list_of_dictionaries.py
$ cat todo_all_employees.json
{"1": [{"username": "Bret", "task": "delectus aut autem", "completed": false}, {"username": "Bret", "task": "quis ut nam facilis et officia qui", "completed": false}, ...], "2": [{"username": "Antonette", "task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": false}, ...], ...}
```

---

## REST API Fundamentals

### What is an API?
An **API (Application Programming Interface)** is a set of rules and protocols that allows different software applications to communicate with each other. It defines the methods and data formats that applications can use to request and exchange information.

### What is a REST API?
**REST (Representational State Transfer)** is an architectural style for designing networked applications. A REST API uses HTTP requests to:
- **GET** - Retrieve data
- **POST** - Create data
- **PUT** - Update data
- **DELETE** - Delete data

### REST API Characteristics
1. **Stateless** - Each request contains all information needed
2. **Client-Server** - Separation of concerns
3. **Cacheable** - Responses can be cached
4. **Uniform Interface** - Consistent way to interact
5. **Layered System** - Client can't tell if connected directly to server

---

## Working with APIs in Python

### Using the Requests Library

#### Installation
```bash
pip install requests
```

#### Basic GET Request
```python
#!/usr/bin/python3
"""Example of API request"""
import requests

# Make GET request
response = requests.get('https://jsonplaceholder.typicode.com/users/1')

# Check status code
if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

#### GET Request with Parameters
```python
import requests

# URL parameters
params = {'userId': 1}
response = requests.get('https://jsonplaceholder.typicode.com/todos', params=params)

# Parse JSON
todos = response.json()
for todo in todos:
    print(f"{todo['id']}: {todo['title']}")
```

#### Accessing JSON Data
```python
import requests

response = requests.get('https://jsonplaceholder.typicode.com/users/1')
user = response.json()

# Access dictionary values safely
user_id = user.get('id')
username = user.get('username')
email = user.get('email')

print(f"User {username} ({email})")
```

---

## Data Formats

### JSON (JavaScript Object Notation)

#### What is JSON?
JSON is a lightweight data interchange format that's easy for humans to read and write, and easy for machines to parse and generate.

#### JSON Structure
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "active": true,
  "skills": ["Python", "JavaScript", "SQL"],
  "address": {
    "city": "New York",
    "country": "USA"
  }
}
```

#### Working with JSON in Python
```python
import json

# Convert Python dict to JSON string
data = {"name": "John", "age": 30}
json_string = json.dumps(data)

# Convert JSON string to Python dict
json_string = '{"name": "John", "age": 30}'
data = json.loads(json_string)

# Write to JSON file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

# Read from JSON file
with open('data.json', 'r') as f:
    data = json.load(f)
```

### CSV (Comma-Separated Values)

#### What is CSV?
CSV is a simple file format used to store tabular data. Each line represents a row, and values are separated by commas.

#### CSV Structure
```csv
id,name,email,active
1,John Doe,john@example.com,true
2,Jane Smith,jane@example.com,false
```

#### Working with CSV in Python
```python
import csv

# Write to CSV
data = [
    ['id', 'name', 'email'],
    [1, 'John', 'john@example.com'],
    [2, 'Jane', 'jane@example.com']
]

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Read from CSV
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Using DictWriter (recommended for this project)
with open('data.csv', 'w', newline='') as f:
    fieldnames = ['id', 'name', 'email']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'id': 1, 'name': 'John', 'email': 'john@example.com'})
```

---

## Python Best Practices

### PEP 8 Style Guide

#### Package and Module Names
```python
# Good
my_package
my_module.py

# Bad
MyPackage
MyModule.py
```

#### Class Names (CapWords/CamelCase)
```python
# Good
class MyClass:
    pass

class APIClient:
    pass

# Bad
class my_class:
    pass

class api_client:
    pass
```

#### Function and Variable Names (lowercase with underscores)
```python
# Good
def my_function():
    pass

user_name = "John"
total_count = 10

# Bad
def MyFunction():
    pass

UserName = "John"
totalCount = 10
```

#### Constants (uppercase with underscores)
```python
# Good
MAX_SIZE = 100
API_BASE_URL = "https://api.example.com"

# Bad
maxSize = 100
ApiBaseUrl = "https://api.example.com"
```

### Import Organization

```python
#!/usr/bin/python3
"""Module documentation"""

# Standard library imports (alphabetical)
import csv
import json
import sys

# Third-party imports (alphabetical)
import requests

# Local imports (alphabetical)
from my_module import my_function
```

### Safe Dictionary Access

```python
# Good - won't throw KeyError
user_id = user.get('id')
username = user.get('username', 'Unknown')

# Bad - throws KeyError if key doesn't exist
user_id = user['id']
```

### Module Execution Guard

```python
#!/usr/bin/python3
"""Module documentation"""

def main():
    """Main function"""
    pass

if __name__ == "__main__":
    main()
```

---

## Code Examples

### Task 0: Gather Data from API

```python
#!/usr/bin/python3
"""
Script to get employee TODO list progress from API
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get employee info
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user = user_response.json()
    employee_name = user.get('name')
    
    # Get todos for employee
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todos = todos_response.json()
    
    # Calculate progress
    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo.get('completed')]
    number_done = len(completed_tasks)
    
    # Print results
    print(f"Employee {employee_name} is done with tasks({number_done}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
```

### Task 1: Export to CSV

```python
#!/usr/bin/python3
"""
Script to export employee TODO list to CSV
"""
import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get employee info
    user = requests.get(f"{base_url}/users/{employee_id}").json()
    username = user.get('username')
    
    # Get todos
    todos = requests.get(f"{base_url}/todos?userId={employee_id}").json()
    
    # Write to CSV
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([
                employee_id,
                username,
                todo.get('completed'),
                todo.get('title')
            ])
```

### Task 2: Export to JSON

```python
#!/usr/bin/python3
"""
Script to export employee TODO list to JSON
"""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get employee info
    user = requests.get(f"{base_url}/users/{employee_id}").json()
    username = user.get('username')
    
    # Get todos
    todos = requests.get(f"{base_url}/todos?userId={employee_id}").json()
    
    # Format data
    tasks = []
    for todo in todos:
        tasks.append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username
        })
    
    # Write to JSON
    filename = f"{employee_id}.json"
    with open(filename, 'w') as jsonfile:
        json.dump({employee_id: tasks}, jsonfile)
```

### Task 3: All Employees to JSON

```python
#!/usr/bin/python3
"""
Script to export all employees TODO lists to JSON
"""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get all users
    users = requests.get(f"{base_url}/users").json()
    
    # Get all todos
    all_todos = requests.get(f"{base_url}/todos").json()
    
    # Organize data
    result = {}
    for user in users:
        user_id = str(user.get('id'))
        username = user.get('username')
        
        # Filter todos for this user
        user_todos = [todo for todo in all_todos if todo.get('userId') == user.get('id')]
        
        # Format tasks
        tasks = []
        for todo in user_todos:
            tasks.append({
                "username": username,
                "task": todo.get('title'),
                "completed": todo.get('completed')
            })
        
        result[user_id] = tasks
    
    # Write to JSON
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(result, jsonfile)
```

---

## Testing Your Scripts

### Manual Testing

```bash
# Task 0
$ python3 0-gather_data_from_an_API.py 1
$ python3 0-gather_data_from_an_API.py 2

# Task 1
$ python3 1-export_to_CSV.py 1
$ cat 1.csv

# Task 2
$ python3 2-export_to_JSON.py 1
$ cat 1.json

# Task 3
$ python3 3-dictionary_of_list_of_dictionaries.py
$ cat todo_all_employees.json
```

### Verify JSON Format

```bash
# Check if JSON is valid
python3 -m json.tool 2.json

# Pretty print JSON
cat 2.json | python3 -m json.tool
```

### Verify CSV Format

```bash
# View CSV
cat 2.csv

# Count lines
wc -l 2.csv

# View in column format
column -t -s ',' 2.csv
```

---

## Common Issues and Solutions

### Issue 1: Module Not Found
```
ModuleNotFoundError: No module named 'requests'
```

**Solution:**
```bash
pip install requests
# or
pip3 install requests
```

### Issue 2: JSON Decode Error
```
json.decoder.JSONDecodeError: Expecting value
```

**Solution:**
```python
# Check response status first
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
else:
    print(f"Error: {response.status_code}")
```

### Issue 3: KeyError
```
KeyError: 'username'
```

**Solution:**
```python
# Use .get() instead of direct access
username = user.get('username')  # Returns None if not found
username = user.get('username', 'Unknown')  # With default value
```

### Issue 4: CSV Quoting Issues

**Solution:**
```python
# Use QUOTE_ALL for consistent quoting
writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
```

### Issue 5: File Encoding Issues

**Solution:**
```python
# Specify encoding explicitly
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)
```

---

## API Best Practices

### 1. Error Handling
```python
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # Raises HTTPError for bad status
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    sys.exit(1)
```

### 2. Use Timeouts
```python
# Prevent hanging requests
response = requests.get(url, timeout=5)
```

### 3. Check Status Codes
```python
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
elif response.status_code == 404:
    print("Not found")
else:
    print(f"Error: {response.status_code}")
```

### 4. Handle Rate Limiting
```python
import time

def get_with_retry(url, max_retries=3):
    for i in range(max_retries):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:  # Too many requests
            time.sleep(2 ** i)  # Exponential backoff
        else:
            break
    return None
```

---

## Resources

- [Friends don't let friends program in shell script](https://www.turnkeylinux.org/blog/friends-dont-let-friends-program-shell-script)
- [What is an API](https://www.webopedia.com/definitions/api/)
- [What is a REST API](https://www.sitepoint.com/rest-api/)
- [What are microservices](https://smartbear.com/learn/api-design/microservices/)
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
- [Python Requests Documentation](https://requests.readthedocs.io/)
- [JSONPlaceholder API](https://jsonplaceholder.typicode.com/)
- [Working with JSON in Python](https://realpython.com/python-json/)
- [Python CSV Module](https://docs.python.org/3/library/csv.html)

## Author
This project is part of the ALX Software Engineering Program.

## License
This project is licensed under the terms of the ALX Software Engineering Program.
