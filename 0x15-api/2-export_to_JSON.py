#!/usr/bin/python3

"""
Module: todo_progress_json
Description: This module retrieves information about an employee's TODO list progress from a REST API and exports it in JSON format.
"""

import json
import requests
import sys


def export_employee_todo_progress(employee_id):
    """
    Retrieve and export the employee's TODO list progress in JSON format.

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

    employee_name = employee_data['username']
    json_data = {str(employee_id): []}

    for todo in todos:
        task_completed = todo['completed']
        task_title = todo['title']
        json_data[str(employee_id)].append({"task": task_title, "completed": task_completed, "username": employee_name})

    json_file = f"{employee_id}.json"

    with open(json_file, 'w') as file:
        json.dump(json_data, file, indent=4)

    print(f"TODO list progress for Employee {employee_name} exported to {json_file}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 todo_progress_json.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_employee_todo_progress(employee_id)
