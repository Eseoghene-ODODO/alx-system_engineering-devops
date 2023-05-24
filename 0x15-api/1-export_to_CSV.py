#!/usr/bin/python3
"""This script uses a REST API to get information about an employee's
TODO list progress and exports it to a CSV file."""

import csv
import requests
import sys


def get_employee_tasks(employee_id):
    """This function takes an employee ID as an argument and exports the
    employee TODO list data to a CSV file."""
    # Make a request to the API with the employee ID
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    # Check if the response is valid
    if response.status_code == 200:
        # Get the employee name from the response
        employee_name = response.json().get("name")
        # Get the employee username from the response
        employee_username = response.json().get("username")
        # Make another request to the API with the employee ID to get the tasks
        response = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}"
            .format(employee_id))
        # Check if the response is valid
        if response.status_code == 200:
            # Get the tasks from the response
            tasks = response.json()
            # Create a list to store the tasks data
            tasks_data = []
            # Loop through the tasks
            for task in tasks:
                # Get the task completed status
                task_completed = task.get("completed")
                # Get the task title
                task_title = task.get("title")
                # Create a dictionary with the task data
                task_data = {
                    "USER_ID": employee_id,
                    "USERNAME": employee_username,
                    "TASK_COMPLETED_STATUS": task_completed,
                    "TASK_TITLE": task_title
                }
                # Append the task data to the list of tasks data
                tasks_data.append(task_data)
            # Create a file name with the employee ID
            file_name = "{}.csv".format(employee_id)
            # Open the file in write mode
            with open(file_name, "w") as file:
                # Create a CSV writer object
                writer = csv.DictWriter(file, fieldnames=task_data.keys(),
                                        quoting=csv.QUOTE_ALL)
                # Write the tasks data to the file
                writer.writerows(tasks_data)
    else:
        # Print an error message if the response is not valid
        print("Error: Invalid response from the API")


if __name__ == "__main__":
    # Check if the argument is an integer
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        # Get the employee ID from the argument
        employee_id = int(sys.argv[1])
        # Call the function with the employee ID
        get_employee_tasks(employee_id)
    else:
        # Print a usage message if the argument is not an integer
        print("Usage: ./1-export_to_CSV.py <employee ID>")
