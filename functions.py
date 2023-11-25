def get_todos(file_path="todos.txt"):
    with open(file_path, "r") as file:
        todos = file.readlines()
        todos = list(set(todos))
    return todos


def write_todos(todos, file_path="todos.txt"):
    with open(file_path, "w") as file:
        todos = list(set(todos))
        file.writelines(todos)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())