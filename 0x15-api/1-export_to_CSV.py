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
    user_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Get the employee's tasks
    tasks_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(employee_id))
    tasks_data = tasks_response.json()

    # Export data to CSV file
    with open("{}.csv".format(employee_id), mode="w", newline="") as csv_file:
        writer = csv.writer(
            csv_file,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_ALL)

        writer.writerow(["USER_ID", "USERNAME",
                         "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in tasks_data:
            task_status = "True" if task.get("completed") else "False"
            task_title = task.get("title")
            writer.writerow([employee_id, employee_name,
                             task_status, task_title])

    # Check 1: Correct user ID and username retrieved
    if employee_name and user_data.get("username"):
        print("User ID and Username: OK")
    else:
        print("User ID and Username: Incorrect")

    # Check 2: Correct output formatting
    with open("{}.csv".format(employee_id), mode="r", newline="") as csv_file:
        reader = csv.reader(
            csv_file,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_ALL)

        # Skip header row
        next(reader)

        task_count = 0
        for i, row in enumerate(reader, start=1):
            if len(row) != 4:
                print("Task {} Formatting: Incorrect".format(i))
            else:
                task_count += 1

        if task_count == len(tasks_data):
            print("Formatting: OK")
        else:
            print("Formatting: Incorrect")

    # Check 3: Correct number of tasks in CSV
    if task_count == len(tasks_data):
        print("Number of tasks in CSV: OK")
    else:
        print("Number of tasks in CSV: Incorrect")
