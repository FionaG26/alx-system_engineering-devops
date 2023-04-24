#!/usr/bin/python3
"""
Extend the Python script in Task 0 to export data in the JSON format
"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    users_url = 'https://jsonplaceholder.typicode.com/users'
    tasks_url = 'https://jsonplaceholder.typicode.com/todos'

    users = requests.get(users_url).json()
    tasks = requests.get(tasks_url).json()

    todo_all_employees = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        todo_all_employees[user_id] = []

        for task in tasks:
            if task.get('userId') == user_id:
                todo = {
                    'username': username,
                    'task': task.get('title'),
                    'completed': task.get('completed'),
                }
                todo_all_employees[user_id].append(todo)

    with open('todo_all_employees.json', mode='w') as file:
        json.dump(todo_all_employees, file)
