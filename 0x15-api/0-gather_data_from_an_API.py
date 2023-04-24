#!/usr/bin/python3
"""
Script that retrieves information about a user's TODO list progress
"""

import requests
import sys


if __name__ == "__main__":
    # API endpoint and user ID
    BASE_URL = "https://jsonplaceholder.typicode.com"
    USER_ID = sys.argv[1]

    # Send request for user info
    user_response = requests.get(BASE_URL + "/users/" + str(USER_ID))
    user_data = user_response.json()
    EMPLOYEE_NAME = user_data["name"]

    # Send request for user's TODO list
    todo_response = requests.get(BASE_URL + "/todos?userId=" + str(USER_ID))
    todo_data = todo_response.json()

    # Count number of completed and total tasks
    completed_tasks = [task for task in todo_data if task["completed"]]
    total_tasks = len(todo_data)
    num_completed_tasks = len(completed_tasks)

    # Print progress report
    print("Employee " + EMPLOYEE_NAME + " is done with tasks(" + str(num_completed_tasks) + "/" + str(total_tasks) + "):")
    for task in completed_tasks:
        print("\t {}".format(task['title']))

