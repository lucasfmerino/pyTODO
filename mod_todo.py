# Módulo de classes - Containers
import id_control as ic


class Container:
    def __init__(self, id:str, path:str, tasks:dict):
        self.id = id
        self.path = path
        self.tasks = tasks

    def new_task(self):
        task_id = ic.new_id()
        task_description = input("Insert the task description: ")
        task = self.tasks[task_id] = task_description
        return task

    def delete_task(self):
        task_id = input("Task id: ")
        if task_id in self.tasks.keys():
            task= self.tasks.pop(task_id)
            return {task_id: task}
        else:
            print("This task don't exist.")

    def move_task(self, container):
        task = self.delete_task()
        if task:
            container.tasks.update(task)
            return task
    
    def task_list(self):
        for task, description in self.tasks.items():
            print(f'{task}:\n{description}')
            print()

    def save_tasks(self):
        with open(self.path, "w") as file:
            for task, description in self.tasks.items():
                file.writelines(f'{task}:{description}\n')

    def record(self):
        with open(self.path, "r") as file:
            task = {item[0]:item[1] for item in [line.rstrip('\n').split(":") for line in file]}
            self.tasks = task


def save_data(containers_list):
    for container in containers_list:
        container.save_tasks()


if __name__ == "__main__":

    container1 = Container("Container1", "data/sprint.txt", {})
    container2 = Container("Container2", "data/done.txt", {})

    container1.record()
    container2.record()

    container1.move_task(container2)

    container1.save_tasks()
    container2.save_tasks()