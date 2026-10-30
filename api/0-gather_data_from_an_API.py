#!/usr/bin/python3

import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    employee_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    employee_response = requests.get(employee_url)
    todos_response = requests.get(todos_url)

    employee = employee_response.json()
    all_tasks = todos_response.json()

    employee_name = employee["name"]

    employee_tasks = [
        task for task in all_tasks
        if task["userId"] == employee_id
    ]

    completed_tasks = [
        task for task in employee_tasks
        if task["completed"]
    ]

    total_tasks = len(employee_tasks)
    number_of_done_tasks = len(completed_tasks)

    print(
        f"Employee {employee_name} is done with tasks"
        f"({number_of_done_tasks}/{total_tasks}):"
    )

    for task in completed_tasks:
        print(f"\t {task['title']}")