#!/usr/bin/python3
"""
Python script to retrieve and display an employee's TODO list progress.
"""

import sys
import requests


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # API endpoint URL
    url = 'https://jsonplaceholder.typicode.com'

    # Make a request to get the employee's information
    employee_url = f'{url}/users/{employee_id}'
    response = requests.get(employee_url)
    employee_data = response.json()

    # Make a request to get the employee's TODO list
    todo_url = f'{url}/todos?userId={employee_id}'
    response = requests.get(todo_url)
    todo_data = response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todo_data if task['completed']]

    # Display employee's TODO list progress
    employee_name = employee_data['name']
    total_tasks = len(todo_data)
    completed_tasks_count = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks
          ({completed_tasks_count}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
