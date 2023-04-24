#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and exports
the data to a CSV file.
"""
import csv
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
    user_name = user_response.get("username")

    print("Employee {} is done with tasks({}/{}):".format(
        user_name, completed_tasks, total_tasks))

    filename = "{}.csv".format(user_id)
    with open(filename, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME",
                        "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_response:
            writer.writerow([user_id, user_name,
                            task.get("completed"), task.get("title")])
