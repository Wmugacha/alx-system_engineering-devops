#!/usr/bin/python3
""" fetches JSON data of Employees from an API"""

import json
import requests


if __name__ == "__main__":
    # Acquire Employee Data

    user_url = "https://jsonplaceholder.typicode.com/users/"

    user_dict = requests.get(user_url).json()

    file_name = "todo_all_employees.json"

    my_dict = {}

    for element in user_dict:
        name = element.get("username")
        user_id = str(element.get("id"))
        user_data = requests.get("{}{}/todos".format(user_url, user_id))
        user_data = user_data.json()
        my_dict[user_id] = []
        for item in user_data:
            inner_dict = {}
            inner_dict["username"] = name
            inner_dict["task"] = item.get("title")
            inner_dict["completed"] = item.get("completed")
            my_dict[user_id].append(inner_dict)

    with open(file_name, 'w') as f:
        json.dump(my_dict, f)
