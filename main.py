user_prompt = "Type add, show, edit or exit: "

todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()
    
    if user_action == "add":
        todo = input("Enter a todo: ")
        todos.append(todo)

    elif user_action == "show":
        for index, item in enumerate(todos):
            print(f"{index + 1} - {item}")

    elif user_action == "edit":
        number = int(input("Number of the todo to edit: "))
        number = number - 1
        new_todo = input("Enter new todo: ")
        todos[number] = new_todo

    elif user_action == "exit":
        break

    else:
        print("Could not understand command")