#!/usr/bin/python3
"""
Python script that uses the requests module to get information about an
employee's TODO list progress using a REST API.
"""

import csv
import requests
import sys


def get_employee_todo_list_progress(user_id):
    """
    Get information about an employee's TODO list progress using a REST API.

    Args:
        user_id (int): The ID of the employee.

    Returns:
        str: The employee TODO list progress in this exact format:
            Employee EMPLOYEE_NAME is done with tasks
            (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
            Second and N next lines display the title of completed tasks:
            TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
    """
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = requests.get(url)
    todos = response.json()
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user_response = requests.get(user_url)
    user = user_response.json()
    done_tasks = [task for task in todos if task.get('completed')]
    return 'Employee {} is done with tasks({}/{}):\n{}'.format(
        user.get('name'), len(done_tasks), len(todos),
        '\n'.join(['\t {}'.format(task.get('title')) for task in done_tasks])
    )


def export_employee_todo_list_to_csv(user_id):
    """
    Export information about an employee's TODO list
    progress to a CSV file using a REST API.

    Args:
        user_id (int): The ID of the employee.
    """
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = requests.get(url)
    todos = response.json()
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user_response = requests.get(user_url)
    user = user_response.json()

    with open('{}.csv'.format(user_id), mode='w') as csv_file:
        fieldN = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for task in todos:
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': user.get('username'),
                'TASK_COMPLETED_STATUS': task.get('completed'),
                'TASK_TITLE': task.get('title')
            })


if __name__ == '__main__':
    export_employee_todo_list_to_csv(int(sys.argv[1]))
