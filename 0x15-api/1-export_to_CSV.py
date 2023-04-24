#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and export
data in CSV format.
"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    # Get the employee ID from the command line arguments
    employee_id = argv[1]

    # Get the employee's name
    user_response = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                                 .format(employee_id))
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Get the employee's tasks
    tasks_response = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                                  .format(employee_id))
    tasks_data = tasks_response.json()

    # Export data to CSV file
    with open("{}.csv".format(employee_id), mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)

        for task in tasks_data:
            task_status = "True" if task.get("completed") else "False"
            task_title = task.get("title")
            writer.writerow([employee_id, employee_name, task_status, task_title])

