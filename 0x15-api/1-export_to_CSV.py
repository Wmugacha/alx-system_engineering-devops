#!/usr/bin/python3
""" fetches JSON data of Employees from an API"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    # Acquire Employee Data

    emp_id = argv[1]

    user_response = requests.get(
                f'https://jsonplaceholder.typicode.com/users/{emp_id}')

    user_data = user_response.json()

    user_name = user_data.get("username")

    todos_response = requests.get(
                f'https://jsonplaceholder.typicode.com/todos?userId={emp_id}')

    user_todos = todos_response.json()

    file_name = emp_id + ".csv"

    with open(file_name, 'w') as csvfile:
        for item in user_todos:
            csvfile.write('"{}","{}","{}","{}"\n'.format(item.get(
                "userId"), user_name, item.get("completed"),
                 item.get("title")))
