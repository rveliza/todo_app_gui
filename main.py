user_prompt = "Type add, show, edit, complete or exit: "


while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()
    
    if user_action == "add":
        todo = input("Enter a todo: ") + "\n"
        
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action == "show":
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(new_todos):
            print(f"{index + 1} - {item}")

    elif user_action == "edit":
        number = int(input("Number of the todo to edit: "))
        number = number - 1
        new_todo = input("Enter new todo: ")
        todos[number] = new_todo
    
    elif user_action == "complete":
        number = int(input("Number of the todo to complete: "))
        todos.pop(number - 1)

    elif user_action == "exit":
        break

    else:
        print("Could not understand command")