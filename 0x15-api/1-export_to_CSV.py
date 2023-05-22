#!/usr/bin/python3

"""
Module: todo_progress_csv
Description: This module retrieves information about an employee's TODO list progress from a REST API and exports it in CSV format.
"""

import csv
import requests
import sys

def export_employee_todo_progress(employee_id):
    """
    Retrieve and export the employee's TODO list progress in CSV format.

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
    csv_file = f"{employee_id}.csv"

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])

        for todo in todos:
            task_completed = str(todo['completed'])
            task_title = todo['title']
            writer.writerow([str(employee_id), employee_name, task_completed, task_title])

    print(f"TODO list progress for Employee {employee_name} exported to {csv_file}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 todo_progress_csv.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_employee_todo_progress(employee_id)
