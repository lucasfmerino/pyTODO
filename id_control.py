
def new_id():
    """
    Returns a new ID as a four-digit string, incrementing the last ID saved in 'data/id.txt' by 1.

    Returns:
    str: A four-digit string containing the new generated ID.

    Raises:
    FileNotFoundError: If the file 'tool_data/id/id.txt' is not found.
    ValueError: If the content of the file 'tool_data/id/id.txt' is not an integer number.
    """
    
    with open('data/id.txt', 'r') as file:
        id = int(file.read())
    id += 1
    with open('data/id.txt', 'w') as file:
        file.writelines((f'{id:0>4}'))
    return f'{id:0>4}'


with open('data/id.txt', 'r') as file:
    id = int(file.read())

id = ((f'{id:0>4}'))


if __name__ == "__main__":
    new_id()
