#!/usr/bin/python3
"""
Exports all tasks from all employees to a JSON file.
"""

import json
import requests
from sys import argv


def export_all_tasks_to_json():
    """
    Exports all tasks from all employees to a JSON file.
    """

    base_url = 'https://jsonplaceholder.typicode.com'
    users_response = requests.get(f'{base_url}/users')
    users = users_response.json()

    all_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        tasks_response = requests.get(f'{base_url}/todos?userId={user_id}')
        tasks = tasks_response.json()
        user_tasks = []

        for task in tasks:
            task_title = task['title']
            completed = task['completed']
            user_tasks.append({
                'username': username,
                'task': task_title,
                'completed': completed
            })

        all_tasks[user_id] = user_tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file)


if __name__ == '__main__':
    export_all_tasks_to_json()
