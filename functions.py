def get_todos(file_path="todos.txt"):
    with open(file_path, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(todos, file_path="todos.txt"):
    with open(file_path, "w") as file:
        file.writelines(todos)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())