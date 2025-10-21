#!/usr/bin/python3
"""
A professional script that fetches and exports all employee TODO tasks
to a JSON file, based on the Single Responsibility Principle.
"""

from sys import argv, exit
import json
import requests


def fetch_user_data(user_id):
    """
    Fetches the data for a specific user.
    Args:
        user_id (int): The employee ID.
    Returns:
        dict: The user's data as a dictionary, or None on failure.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for 4xx/5xx errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user data: {e}")
        return None


def fetch_user_todos(user_id):
    """
    Fetches all TODO tasks for a specific user ID.
    Args:
        user_id (int): The employee ID.
    Returns:
        list: A list of tasks (dictionaries), or None on failure.
    """
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching todos data: {e}")
        return None


def export_to_json(user_data, todos_list):
    """
    Exports all user tasks to a JSON file in the required format.
    
    Format: { "USER_ID": [
        {"task": "TASK_TITLE", "completed": TASK_COMPLETED, "username": "USERNAME"},
        ...
    ]}

    Args:
        user_data (dict): User information dictionary.
        todos_list (list): List of task dictionaries to export.
    """
    user_id = user_data.get("id")
    username = user_data.get("username")

    if not user_id or not username or todos_list is None:
        print("Missing user data or todos, cannot export to JSON.")
        return

    json_task_list = []
    for task in todos_list:
        json_task_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    json_output = {user_id: json_task_list}

    filename = f"{user_id}.json"

    try:
        with open(filename, "w", encoding="UTF-8") as f:
            json.dump(json_output, f)
    except IOError as e:
        print(f"Error writing to JSON file: {e}")


def main():
    """
    The "Center" (Orchestrator).
    Manages the application flow.
    """
    # 1. Handle Inputs
    if len(argv) != 2:
        print(f"Usage: {argv[0]} <employee_id>")
        exit(1)
        
    try:
        employee_id = int(argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        exit(1)

    # 2. Orchestrate Logic (Call functions)
    user_data = fetch_user_data(employee_id)
    if not user_data:
        exit(1)  # Error already printed by the function

    user_id = user_data.get("id")
    todos_list = fetch_user_todos(user_id)
    if todos_list is None:  # Check for None, as [] (empty list) is valid
        exit(1)

    # 3. Handle Presentation (Export to JSON)
    export_to_json(user_data, todos_list)


if __name__ == "__main__":
    main()
