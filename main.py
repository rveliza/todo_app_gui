user_prompt = "Type add, show, edit, complete or exit: "


while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()
    
    if "add" in user_action:
        todo = user_action[4:]
        
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif "show" in user_action:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(new_todos):
            print(f"{index + 1} - {item}")

    elif "edit" in user_action:
        number = int(input("Number of the todo to edit: "))
        number = number - 1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + "\n"

        with open("todos.txt", "w") as file:
            file.writelines(todos)
    
    elif "complete" in user_action:
        number = int(input("Number of the todo to complete: "))

        with open("todos.txt", "r") as file:
            todos = file.readlines()


        removed_todo = todos.pop(number - 1).strip("\n")


        with open("todos.txt", "w") as file:
            file.writelines(todos)

        message = f"Todo {removed_todo} was removed from the list."
        print(message)

    elif "exit" in user_action:
        break

    else:
        print("Could not understand command")