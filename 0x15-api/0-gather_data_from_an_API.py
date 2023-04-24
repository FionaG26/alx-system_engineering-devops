#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todo_url = ("https://jsonplaceholder.typicode.com/todos?"
                "userId={}".format(user_id))

    user_response = requests.get(user_url).json()
    todo_response = requests.get(todo_url).json()

    total_tasks = len(todo_response)
    completed_tasks = sum(task.get("completed") for task in todo_response)
    user_name = user_response.get("name")

    print("Employee {} is done with tasks({}/{}):".format(
        user_name, completed_tasks, total_tasks))

    for task in todo_response:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))
