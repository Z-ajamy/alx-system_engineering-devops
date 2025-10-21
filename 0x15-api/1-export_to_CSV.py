#!/usr/bin/python3
"""Employee TODO progress tracker with CSV export functionality.

This professional script fetches and displays an employee's TODO list progress
from the JSONPlaceholder API, following the Single Responsibility Principle.
It provides task completion statistics and exports data to CSV format.
"""

from sys import argv, exit
import requests
import csv


def fetch_user_data(user_id):
    """Fetch user information from the API.
    
    Retrieves detailed information about a specific user by their ID from
    the JSONPlaceholder API endpoint.
    
    Args:
        user_id (int): The unique identifier for the employee.
    
    Returns:
        dict: User data including id, name, and other profile information.
            Returns None if the request fails.
    
    Examples:
        >>> user = fetch_user_data(1)
        >>> print(user['name'])
        'Leanne Graham'
    """
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve user data: {e}")
        return None


def fetch_user_todos(user_id):
    """Fetch all TODO tasks for a specific user.
    
    Retrieves the complete list of TODO items associated with a user from
    the JSONPlaceholder API todos endpoint.
    
    Args:
        user_id (int): The unique identifier for the employee.
    
    Returns:
        list: List of task dictionaries containing title, completed status, etc.
            Returns None if the request fails.
    
    Examples:
        >>> todos = fetch_user_todos(1)
        >>> len(todos)
        20
    """
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve TODO list: {e}")
        return None


def process_tasks(todos_list):
    """Analyze task list and calculate completion statistics.
    
    Pure function that processes a list of tasks and extracts metrics including
    total count, completed count, and titles of completed tasks.
    
    Args:
        todos_list (list): List of task dictionaries with 'title' and 'completed' keys.
    
    Returns:
        dict: Dictionary containing:
            - done_count (int): Number of completed tasks
            - total_tasks (int): Total number of tasks
            - done_titles (list): List of completed task titles
    
    Examples:
        >>> tasks = [{'title': 'Task 1', 'completed': True}]
        >>> result = process_tasks(tasks)
        >>> result['done_count']
        1
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
    """Display task completion progress to console.
    
    Formats and prints the employee's task completion statistics and
    lists all completed task titles.
    
    Args:
        user_data (dict): User information dictionary containing 'name' key.
        task_progress (dict): Processed task statistics from process_tasks().
    
    Examples:
        >>> display_progress({'name': 'John'}, {'done_count': 5, 'total_tasks': 10, 'done_titles': []})
        Employee John has completed 5/10 tasks:
    """
    employee_name = user_data.get("name", "Unknown Employee")
    done = task_progress.get("done_count")
    total = task_progress.get("total_tasks")
    titles = task_progress.get("done_titles")

    print(f"Employee {employee_name} has completed {done}/{total} tasks:")
    for title in titles:
        print(f"\t {title}")

def export_to_csv(user_data, todos_list):
    """Export task data to CSV file in the format required by the checker.
    
    Creates a CSV file named {user_id}.csv with columns for
    user ID, username, completion status, and task title.
    
    Args:
        user_data (dict): User info dictionary containing 'id' and 'username'.
        data_list (list): List of task dictionaries to export.
    """
    user_id = user_data.get("id")
    username = user_data.get("username")

    if not user_id or not username or todos_list is None:
        return 

    filename = f"{user_id}.csv"
    
    try:
        with open(filename, "w", encoding="UTF-8", newline='') as f:
            
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            
            for task in todos_list:
                writer.writerow([
                    user_id,
                    username,
                    task.get("completed"),
                    task.get("title")
                ])
    except IOError as e:
        print(f"Error writing to CSV file: {e}")



def main():
    """Application entry point and orchestrator.
    
    Coordinates the entire workflow: validates input, fetches data from API,
    processes task statistics, displays results, and exports to CSV.
    
    Raises:
        SystemExit: If invalid arguments provided or API requests fail.
    """
    if len(argv) != 2:
        print(f"Usage: {argv[0]} <employee_id>")
        exit(1)
        
    try:
        employee_id = int(argv[1])
    except ValueError:
        print("Error: Employee ID must be a valid integer.")
        exit(1)

    user_data = fetch_user_data(employee_id)
    if not user_data:
        exit(1)

    user_id = user_data.get("id")
    todos_list = fetch_user_todos(user_id)
    if todos_list is None:
        exit(1)

    task_progress = process_tasks(todos_list)

    export_to_csv(user_data, todos_list)


if __name__ == "__main__":
    main()
