#!/usr/bin/python3
"""This script fetches JSON data from an API to retrieve information
   about a given employee's progress on their TODO list.
"""

import requests
from sys import argv

if __name__ == "__main__":
    # Acquire Employee Data

    emp_id = int(argv[1])

    response = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{emp_id}')

    data = response.json()

    name = data['name']

    response = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={emp_id}')

    todos = response.json()

    completed_todos = sum(todo['completed'] for todo in todos)

    total_todos = len(todos)

    print(f"Employee {name} is done with tasks"
          f"({completed_todos}/{total_todos}):")

    for todo in todos:
        if todo['completed']:
            print('\t' + ' ' + todo['title'])
