#!/usr/bin/python3
"""
Module: export_to_CSV

This module fetches to-do list information for a given employee ID from the
JSONPlaceholder API and exports the data to a CSV file.

The CSV file will be named '<employee_id>.csv' and will contain the following
fields for each to-do item:
- Employee ID
- Username
- Completion status of the to-do item
- Title of the to-do item
"""

import csv
import requests
import sys


def main():
    """Main function to execute the script's logic.

    This function processes the command-line argument to get the employee ID,
    fetches the employee's username and to-do list from the API, and exports
    the to-do list to a CSV file.

    Command-line arguments:
        <employee_id> (int): The ID of the employee whose to-do list is to be
        fetched.

    Exits:
        Exits with code 1 if the number of arguments is incorrect, if the
        employee ID is not an integer, or if the API requests fail.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
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

    filename = f"{user_id}.csv"
    with open(filename, "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([
                user_id,
                username,
                todo.get("completed"),
                todo.get("title")
            ])

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    main()
