#!/usr/bin/python3

"""
Module: todo_progress
Description: This module retrieves information about an employee's
TODO list progress from a REST API.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieve and display the employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    if 'id' not in employee_data:
        print(f"Employee with ID {employee_id} not found.")
        return

    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo.get('completed'))

    employee_name = employee_data.get('name')

    print(f"Employee {employee_name} is done with tasks "
          f"({completed_tasks}/{total_tasks}):")
    for todo in todos:
        if todo.get('completed'):
            print(f"\t{todo.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 todo_progress.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
