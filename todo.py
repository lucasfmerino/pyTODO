from mod_todo import *


# LOAD THE PROGRAM
backlog = Container("Container1", "data/backlog.txt", {})
sprint = Container("Container2", "data/sprint.txt", {})
done = Container("Container3", "data/done.txt", {})

backlog.record()
sprint.record()
done.record()

containers = [backlog, sprint, done]


# WELCOME INTERFACE
print("WELCOME TO PYTODO")
print()


# FIRST STEP - CHOOSE A CONTAINER:
exit = False
while not exit:

    operation_01 = input(
'''
Choose a container option: 

1 - Backlog container
2 - Sprint container
3 - Done container
4 - Exit

'''
)
    print()

    if operation_01 == "1":
        container = backlog

    elif operation_01 == "2":
        container = sprint

    elif operation_01 == "3":
        container = done

    elif operation_01 == "4":
        exit = True
        continue

    else:
        print("Invalid Operation")
        continue


# SECOND STEP - CHOOSE A ACTION:

    print()

    back = False
    while not back:

        operation_02 = input(
    '''Choose a task option: 
    1 - List tasks
    2 - Add a new task
    3 - Delete a task
    4 - Move a task
    5 - Back
    6 - Exit

    '''
    )

        if operation_02 == "1":
            print()
            container.task_list()
            print()
            input("Press enter to continue: ")
            continue

        elif operation_02 == "2":
            print("NEW TASK")
            print()
            container.new_task()
            save_data(containers)
            print()
            continue

        elif operation_02 == "3":
            print("DELETE A TASK")
            print()
            container.delete_task()
            save_data(containers)
            print()
            continue

        elif operation_02 == "4":
            print()
            print("MOVE A TASK")
            while True:
                move = input(
    """
    Where do you want to move the task?

    1 - To Backlog container
    2 - To Sprint container
    3 - To Done container
    4 - Cancel

    """
        )

                if move == "1":
                    move = backlog
                elif move == "2":
                    move  = sprint
                elif move == "3":
                    move = done
                elif move == "4":
                    print("Operation canceled.")
                    print()
                    break
                else:
                    print("Invalid Operation")
                    continue

                container.move_task(move)
                save_data(containers)
                print()
                break

        elif operation_02 == "5":
            back = True
            continue

        elif operation_02 == "6":
            exit = True
            break

        else:
            print("Invalid Operation")
        continue


# END STEP - SAVE

save_data(containers)
print()
print("Thankyou to use PYTODO")
