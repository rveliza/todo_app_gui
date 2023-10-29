user_prompt = "Type add, show or exit: "

todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()
    
    if user_action == "add":
        todo = input("Enter a todo: ")
        todos.append(todo)
    elif user_action == "show":
        print(todos)
    elif user_action == "exit":
        break
    else:
        print("Could not understand command")