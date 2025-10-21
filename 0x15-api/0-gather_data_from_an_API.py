#!/usr/bin/python3
"""Employee TODO progress tracker.

This script fetches and displays an employee's completed tasks from the
JSONPlaceholder API. It takes an employee ID as a command-line argument
and shows their task completion statistics along with a list of all
completed task titles.

The script validates the input, makes HTTP requests to fetch user and
todo data, filters completed tasks, and displays formatted results.

Example:
    $ python3 script.py 1
    Output:
    Employee Leanne Graham has completed 11/20 tasks
         delectus aut autem
         quis ut nam facilis et officia qui
         ...

Requirements:
    - requests library for HTTP API calls
    - Internet connection to access JSONPlaceholder API
    - Valid employee ID (integer) as command-line argument

API Endpoints:
    - Users: https://jsonplaceholder.typicode.com/users/{id}
    - Todos: https://jsonplaceholder.typicode.com/todos?userId={id}

Expected Output Format:
    - Summary line: "Employee {name} has completed {done}/{total} tasks"
    - Individual completed tasks: tab-indented task titles
"""

from sys import argv
import requests


if len(argv) == 2:
    """Main execution block for employee TODO tracking.
    
    This block performs the following operations:
    1. Validates that exactly 2 arguments are provided (script name + employee ID)
    2. Parses and validates the employee ID as an integer
    3. Fetches user information from the API
    4. Fetches all TODO items for the user
    5. Filters completed tasks and displays results
    
    The script uses nested conditional checks to ensure data validity at each
    step before proceeding to the next API call or operation.
    
    Validation Steps:
        - Argument count check (must be exactly 2)
        - Integer conversion of employee ID
        - HTTP 200 status code verification
        - User ID existence check
        - TODO list availability check
    
    Error Handling:
        - ValueError: Invalid integer input, prints error and exits with code 1
        - HTTP errors: Silent failure (no output if API calls fail)
    """

    try:
        arg = int(argv[1])
    except ValueError as e:
        print(e)
        exit(1)

    api_users_endpoint = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    response_user = requests.get(api_users_endpoint)
    if response_user.status_code == 200:
        user_dict = response_user.json()
        user_id = user_dict.get("id", None)

        if user_id:
            api_todos_endpoint = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
            response_todos = requests.get(api_todos_endpoint)

            if response_todos.status_code == 200:
                todos_dict = response_todos.json()

                if todos_dict:
                    done_list = []

                    for task in todos_dict:
                        if task["completed"] == True:
                            done_list.append(task["title"])

                    print("Employee {} has completed {}/{} tasks:".format(user_dict["name"], len(done_list), len(todos_dict)))
                    for title in done_list:
                        print("\t {}".format(title))
