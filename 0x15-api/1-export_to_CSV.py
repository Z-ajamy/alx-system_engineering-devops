#!/usr/bin/python3
"""
Module: export_to_CSV

This module fetches tasks for a specific employee from the JSONPlaceholder API
and exports the data to a CSV file.

The CSV file includes the employee ID, username, completion status of each task
and the task title.
"""

import csv
import requests
import sys


def main():
    """Main function to execute the script's logic.

    This function processes the command-line argument to get the employee ID,
    fetches the employee's details and tasks from the API, and exports the
    tasks to a CSV file named '<employee_id>.csv'.

    Command-line arguments:
        <employee_id> (int): The ID of the employee whose tasks are to be
        fetched.

    Exits:
        Exits with code 1 if the number of arguments is incorrect, if the
        employee ID is not an integer, or if the API requests fail.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
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

    username = user.get("username")

    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([
                employee_id,
                username,
                todo.get("completed"),
                todo.get("title")
            ])

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    main()
