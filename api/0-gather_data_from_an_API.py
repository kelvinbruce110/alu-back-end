#!/usr/bin/python3
"""Gather TODO list progress for a single employee."""

import sys

import requests


def main():
    """Display an employee's completed TODO tasks."""
    employee_id = int(sys.argv[1])

    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(employee_id)
    )
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    response = requests.get(user_url)

    if response.status_code != 200:
        return

    user_data = response.json()

    todos_response = requests.get(
        todos_url,
        params={"userId": employee_id}
    )

    if todos_response.status_code != 200:
        return

    todos = todos_response.json()

    completed_tasks = [
        task for task in todos if task.get("completed")
    ]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user_data.get("name"),
            len(completed_tasks),
            len(todos)
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()