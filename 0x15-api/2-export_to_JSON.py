#!/usr/bin/env python3

import json
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: {} <employee_id>".format(sys.argv[0]))
    sys.exit(1)

employee_id = sys.argv[1]
response = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id))
tasks = response.json()

user_response = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
user = user_response.json()
username = user['username']

data = {employee_id: []}
for task in tasks:
    data[employee_id].append({
        'task': task['title'],
        'completed': task['completed'],
        'username': username
    })

with open('{}.json'.format(employee_id), 'w') as f:
    json.dump(data, f)

