# Description
PyTODO is a Python program that allows users to create, manage, and organize tasks in different containers, such as a backlog or a sprint. It consists of three modules, which are described below.

## Module 1 - id_control
The id_control module provides a function new_id() that returns a new ID as a four-digit string, incrementing the last ID saved in the file 'data/id.txt' by 1. If the file 'data/id.txt' is not found, it raises a FileNotFoundError. If the content of the file 'data/id.txt' is not an integer number, it raises a ValueError.

## Module 2 - mod_todo
The mod_todo module contains the Container class, which is used to create containers to store tasks. Each container has an ID, a file path to save the tasks, and a dictionary to store the tasks.

The Container class has the following methods:

new_task(): Creates a new task in the container and returns the task's description.
delete_task(): Deletes a task from the container and returns the deleted task.
move_task(container): Moves a task from the current container to another container and returns the moved task.
task_list(): Lists all the tasks in the container.
save_tasks(): Saves all the tasks in the container to the file specified in the container's path.
record(): Loads all the tasks in the container from the file specified in the container's path.
The save_data(containers_list) function is also provided to save all the tasks in the containers in the containers_list to their respective files.

## Module 3 - main
The main module is the main program that uses the id_control and mod_todo modules to create and manage the containers and tasks.

When the program starts, it loads the tasks from the files specified in the Container instances and presents the user with a welcome interface. The user can choose a container to work with and then choose an action to perform, such as adding or deleting a task, or moving a task to another container. When the user finishes working with a container, the program saves all the tasks in the container to its file.

# Usage
To use PyTODO, run the main.py file. You will be presented with a welcome interface and a list of options to choose from. Follow the prompts to create and manage containers and tasks.

# Requirements
Python 3.7 or higher.

# License
This project is licensed under the MIT License. See the LICENSE file for details.