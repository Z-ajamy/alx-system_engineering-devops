#!/usr/bin/python3
import json

"""
Module: write_todo_data

This module writes a dictionary of to-do list data to a JSON file.

The data is organized by employee IDs, with each ID mapping to a list of
tasks associated with that employee. Each task includes the username of the
employee, the task title, and whether the task is completed.

Example data format:
{
    "1": [
        {"username": "Bret", "task": "delectus aut autem", "completed": False},
        {"username": "Bret", "task": "quis ut nam facilis et officia qui",
        "completed": False}
    ],
    "2": [
        {"username": "Antonette", "task": "suscipit repellat esse quibusdam
        voluptatem incidunt", "completed": False},
        {"username": "Antonette", "task": "distinctio vitae autem nihil ut
        molestias quo", "completed": True}
    ]
}
"""

# Example data in the required format
data = {
    "1": [
        {"username": "Bret", "task": "delectus aut autem", "completed": False},
        {"username": "Bret", "task": "quis ut nam facilis et officia qui",
         "completed": False},
        # Add more tasks here...
    ],
    "2": [
        {"username": "Antonette", "task":
         "suscipit repellat esse quibusdamvoluptatem incidunt", "completed":
         False},
        {"username": "Antonette", "task":
         "distinctio vitae autem nihil ut molestias quo", "completed": True},
        # Add more tasks here...
    ],
    # Add more user data here...
}

# File name
file_name = 'todo_all_employees.json'

# Write data to JSON file
with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)

print(f"Data has been written to {file_name}")
