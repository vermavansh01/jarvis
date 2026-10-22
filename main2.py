import calculator
import command
import random
import os

print('🤖 JARVIS: Hello! What is your name?')
name = input('👤 You: ')

while name == '':
    name = input("🤖 JARVIS: Enter your name!")

print(f'\n🤖 JARVIS: Nice to meet you, {name}!')

exit_responses = [
    "Goodbye",
    "See you later",
    "Bye",
    "Take care"
]

while True:
    user = input("\n👤 You: ").lower().strip()
    if user in calculator.operations :
        operation = calculator.operations[user]
        result = calculator.calculation(operation)
        calculator.set_operation_count(user)
        print(result)

    elif user in calculator.other_opeations:
        operation = calculator.other_opeations[user]
        operation()

    elif user in command.commands :
        cmd = command.commands[user]
        result = command.run_command(cmd,name)
        print(result)

    elif "history" in user:
        if user == "history":
            len_history = len(calculator.history)
            calculator.view_history(len_history)
        else:
            his = user.split()
            try:
                calculator.view_history(int(his[1]))

            except ValueError:
                print("🤖 JARVIS: Please enter a valid integer Just after history")

    elif "remember" in user:
        if user == "remember":
            print("🤖 JARVIS: Please enter a valid syntax (Example: remember 100)")

        else:
            value = user.split()
            command.remember(value[1])

    elif "note" in user :
        if user == "notes":
            command.get_note()
        
        elif user.startswith("note "):
            value = user.split()
            command.add_note(" ".join(value[1:]))

        elif user.startswith("delete note "):
            try:
                position = user.split()
                command.delete_note(int(position[2]))

            except ValueError:
                print("🤖 JARVIS: Please enter a valid integer Just after delete note")

        elif user.startswith("edit note "):
            position = user.split()
            if len(position) < 4 :
                print("🤖 JARVIS: Please enter the new note.")

            else:
                try:
                    command.edit_note(
                        int(position[2]),
                        " ".join(position[3:])
                    )

                except ValueError:
                    print("🤖 JARVIS: Please enter a valid integer Just after edit note")

        elif user == "load notes":
            command.load_notes()
            
        elif user == "notes clear":
            command.clear_notes()  

        else:
            print("🤖 JARVIS: Please enter a note.")

    elif user.startswith("find "):
        value = user.split()
        command.search_note(" ".join(value[1:]))

    elif user == "help":
        print("🤖 JARVIS: Available commands:")
        print()

        print("Normal Commands:")
        for item in command.commands:
            print(item)

        print()
        print("Calculator Commands:")
        for item in calculator.operations:
            print(item)
        for item in calculator.other_opeations:
            print(item)

        print("exit") 

    elif user == "clear":
        os.system("cls")
        print("\n🤖 JARVIS: Screen cleared!")

    elif user == "exit" :
        print(f"\n🤖 JARVIS: {random.choice(exit_responses)} {name}!")
        break

    else:
        print ("🤖 JARVIS: I don't understand that yet")