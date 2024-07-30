#!/usr/bin/python3
"""
Module: gather_data_from_an_API

This module retrieves and displays tasks for a specific employee from the
JSONPlaceholder API.
"""

import requests
import sys


def main():
    """Main function to execute the script's logic.

    This function processes the command-line argument to get the employee ID,
    fetches the employee's details and tasks from the API, and prints a summary
    of completed tasks and the total number of tasks.

    Command-line arguments:
        <employee_id> (int): The ID of the employee whose tasks are to be
        fetched.

    Exits:
        Exits with code 1 if the number of arguments is incorrect, if the
        employee ID is not an integer, or if the API requests fail.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    user_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if (user_response.status_code != 200 or
            todos_response.status_code != 200):
        print("Error: Unable to fetch data from the API")
        sys.exit(1)

    user = user_response.json()
    todos = todos_response.json()

    employee_name = user.get("name")
    completed_tasks = [
        todo.get("title") for todo in todos if todo.get("completed")
    ]
    total_tasks = len(todos)

    print(
        f"Employee {employee_name} is done with tasks({len(completed_tasks)}/"
        f"{total_tasks}):"
    )
    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    main()
