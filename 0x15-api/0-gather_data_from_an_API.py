#!/usr/bin/python3
""" fetches JSON data of Employees from an API"""

import requests
from sys import argv

if __name__ == "__main__":
    # Acquire Employee Data

    emp_id = int(argv[1])

    user_response = requests.get(
                f'https://jsonplaceholder.typicode.com/users/{emp_id}')

    user_data = user_response.json()

    user_name = user_data.get("name")

    todos_response = requests.get(
                f'https://jsonplaceholder.typicode.com/todos?userId={emp_id}')

    user_todos = todos_response.json()

    c_todos = sum(todo['completed'] for todo in user_todos)

    total_todos = len(user_todos)

    print(
        f"Employee {user_name} is done with tasks({c_todos}/{total_todos}):")

    for todo in user_todos:
        if todo['completed']:
            print('\t' + ' ' + todo['title'])
