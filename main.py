from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is now ", now)

user_prompt = "Type add, show, edit, complete or exit: "

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()
    
    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + "\n")

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(new_todos):
            print(f"{index + 1} - {item}")

    elif user_action.startswith("edit"):

        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)
                
        except ValueError:
            print("Your command is not valid")
    
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            removed_todo = todos.pop(number - 1).strip("\n")

            write_todos(todos)

            message = f"Todo {removed_todo} was removed from the list."
            print(message)
        
        except IndexError:
            print("There is no item with that number")

    elif user_action.startswith("exit"):
        break

    else:
        print("Could not understand command")