#!/usr/bin/python3
"""
This script fetches JSON data from an API to retrieve information
about a given employee's progress on their TODO list.
"""

import requests
import sys

if __name__ == "__main__":

    emp_id = int(sys.argv[1])

    response = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{emp_id}')

    if response.status_code == 200:
        data = response.json()

        name = data['name']

        response = requests.get(
                f'https://jsonplaceholder.typicode.com/todos?userId={emp_id}')

        if response.status_code == 200:

            todos = response.json()

            completed_todos = sum(todo['completed'] for todo in todos)

            total_todos = len(todos)

            print(f"Employee {name} is done with "
                  f"{completed_todos}/{total_todos} tasks:")

            for todo in todos:
                if todo['completed']:
                    print('\t ' + todo['title'])
