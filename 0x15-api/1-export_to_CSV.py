#!/usr/bin/python3

from sys import argv
import requests

if len(argv) == 2:

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

                    print("Employee {} is done with tasks ({}/{})".format(user_dict["name"], len(done_list), len(todos_dict)))
                    for title in done_list:
                        print("\t {}".format(title))
