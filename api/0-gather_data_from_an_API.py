#!/usr/bin/python3
"""Shows the TODO list progress of an employee using a REST API."""
import requests
import sys


def get_todo_progress(employee_id):
    """Prints the name of the employee and the tasks they have finished."""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos".format(base_url)

    user = requests.get(user_url).json()
    todos = requests.get(todos_url, params={"userId": employee_id}).json()

    name = user.get("name")
    done = [task for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(done), len(todos)))
    for task in done:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_todo_progress(int(sys.argv[1]))