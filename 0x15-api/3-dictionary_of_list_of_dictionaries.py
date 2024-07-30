#!/usr/bin/python3
"""
Module: export_all_to_json

This module fetches to-do list information for all employees from the
JSONPlaceholder API and exports the data to a JSON file named
'todo_all_employees.json'.

The data is organized by employee IDs, with each ID mapping to a list of
tasks associated with that employee. Each task includes the username of the
employee, the task title, and whether the task is completed.
"""

import json
import requests


def fetch_data():
    """Fetches user and task data from the API.

    This function retrieves user information and tasks for each user from
    the JSONPlaceholder API. It creates a dictionary where the keys are user
    IDs and the values are lists of tasks associated with each user. Each
    task is represented as a dictionary containing the task title, completion
    status, and the username of the employee.

    Returns:
        dict: A dictionary where each key is a user ID and the value is a
        list of task dictionaries with the structure:
        [
            {
                "task": "Title of the to-do item",
                "completed": true/false,
                "username": "Username of the employee"
            },
            ...
        ]
    """
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    user_response = requests.get(f"{base_url}users")
    users = user_response.json()

    # Dictionary to hold user ID and their tasks
    data = {}

    # Fetch tasks for each user
    for user in users:
        user_id = user["id"]
        username = user["username"]
        tasks_response = requests.get(f"{base_url}todos", params={"userId":
                                                                  user_id})
        tasks = tasks_response.json()

        # Process tasks for the user
        data[user_id] = [{
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        } for task in tasks]

    return data


def save_to_file(data):
    """Saves the data to a JSON file.

    Args:
        data (dict): The data to be written to the file. It should be a
        dictionary where each key is a user ID and the value is a list of
        task dictionaries.
    """
    with open("todo_all_employees.json", "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    todo_data = fetch_data()
    save_to_file(todo_data)
