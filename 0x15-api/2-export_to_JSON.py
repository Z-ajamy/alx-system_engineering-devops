#!/usr/bin/python3
"""
Module: export_to_JSON

This module fetches to-do list information for a given employee ID from the
JSONPlaceholder API and exports the data to a JSON file.

The JSON file will be named '<employee_id>.json' and will contain the following
format:
{
    "<employee_id>": [
        {
            "task": "Title of the to-do item",
            "completed": true/false,
            "username": "Username of the employee"
        },
        ...
    ]
}
"""

import json
import requests
import sys


def main():
    """Main function to execute the script's logic.

    This function processes the command-line argument to get the employee ID,
    fetches the employee's username and to-do list from the API, and exports
    the to-do list to a JSON file.

    Command-line arguments:
        <employee_id> (int): The ID of the employee whose to-do list is to be
        fetched.

    Exits:
        Exits with code 1 if the number of arguments is incorrect, if the
        employee ID is not an integer, or if the API requests fail.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(f"{url}users/{user_id}")

    if user_response.status_code != 200:
        print("Error: Unable to fetch user data")
        sys.exit(1)

    user = user_response.json()
    username = user.get("username")

    todos_response = requests.get(f"{url}todos", params={"userId": user_id})

    if todos_response.status_code != 200:
        print("Error: Unable to fetch todos data")
        sys.exit(1)

    todos = todos_response.json()

    tasks = [
        {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        }
        for todo in todos
    ]

    data = {str(user_id): tasks}

    with open(f"{user_id}.json", "w", encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)

    print(f"Data exported to {user_id}.json")


if __name__ == "__main__":
    main()
