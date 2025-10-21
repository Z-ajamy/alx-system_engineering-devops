#!/usr/bin/python3
"""
A professional script that fetches and displays TODO list progress
based on the Single Responsibility Principle.
"""

from sys import argv, exit
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

def process_tasks(todos_list):
    """
    Analyzes a list of tasks and extracts progress. (Pure function)
    Args:
        todos_list (list): A list of task dictionaries.
    Returns:
        dict: A dictionary containing processed task info.
    """
    if not isinstance(todos_list, list):
        return {"done_count": 0, "total_tasks": 0, "done_titles": []}

    total_tasks = len(todos_list)
    done_titles = [
        task.get("title") for task in todos_list if task.get("completed")
    ]
    done_count = len(done_titles)

    return {
        "done_count": done_count,
        "total_tasks": total_tasks,
        "done_titles": done_titles
    }

def display_progress(user_data, task_progress):
    """
    Handles the presentation (printing) of the results.
    Args:
        user_data (dict): The dictionary for the user.
        task_progress (dict): The processed task info.
    """
    employee_name = user_data.get("name", "Unknown Employee")
    done = task_progress.get("done_count")
    total = task_progress.get("total_tasks")
    titles = task_progress.get("done_titles")

    print(f"Employee {employee_name} is done with tasks ({done}/{total}):")
    for title in titles:
        print(f"\t {title}")

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
        exit(1) # Error already printed by the function

    # We can use the ID from the validated user_data
    user_id = user_data.get("id")
    todos_list = fetch_user_todos(user_id)
    if todos_list is None: # Check for None, as [] (empty list) is valid
        exit(1)

    task_progress = process_tasks(todos_list)

    # 3. Handle Presentation
    display_progress(user_data, task_progress)

if __name__ == "__main__":
    main()
