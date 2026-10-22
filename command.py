import datetime as time
import random
import json

memory = []
notes = []

def say_hello(name):
    return f"{random.choice(hello_responses)} {name}"

def how_am_i(name):
    return f"{random.choice(how_are_you_responses)}, {name}!"

def who_am_i():
    return "I am JARVIS, your personal Python assistant."

def current_time():
    c_time = time.datetime.now().strftime("%H:%M:%S")
    return f"The current time is {c_time}"

def today_date():
    t_date = time.datetime.now().strftime("%d-%m-%Y")
    return f"Today's date is {t_date}"

def calculate_age():
    while True:
        try:
            print("🤖 JARVIS: Enter your birth year")
            birth_year = int(input("👤 You: "))
            age = time.datetime.now().year - birth_year
            return f"You are approximately {age} years old."
        except ValueError:
            print("🤖 JARVIS: Please enter a valid integer")

def joke():
    return random.choice(jokes)

def remember(value):
    memory.clear()
    memory.append(value)
    print(f"{value} stored in memory.")

def get_memory():
    if not memory:
        print ("🤖 JARVIS: No memory stored yet.")
        
    return f" Memory → {memory[0]}"

def delete_memory():
    memory.clear()
    return "Memory cleared."

def add_note(value):
    notes.append(value)
    print("🤖 JARVIS: Note added.")

def get_note():
    print("\n🤖 JARVIS: Saved notes")
    i1 = 1

    with open("notes.json","r") as file:
        saved_notes = json.load(file)

        if not saved_notes:
            print("🤖 JARVIS: No notes yet")

        for line in saved_notes:
            print(f"{i1} → {line}")
            i1 += 1

    print("\n🤖 JARVIS: Current notes")
    if not notes:
        print("🤖 JARVIS: No notes yet")

    i2 = 1
    for item in notes:
        print(f"{i2} → {item}")
        i2 += 1

def search_note(value):
    found = False
    i = 1
    for item in notes:
        if value in item:
            print(f"🤖 JARVIS: {i} → {item}")
            i += 1
            found = True

    if not found:  
        print("🤖 JARVIS: I couldn't find any matching notes.")

def delete_note(position):
    if position <= 0:
        print("🤖 JARVIS: Invalid note number.")

    elif position > len(notes):
        print("🤖 JARVIS: Note number doesn't exist.")

    else:
        result = notes.pop(position - 1)
        print(f"🤖 JARVIS: Deleted: {result}")

def edit_note(position, value):
    if position <= 0:
        print("🤖 JARVIS: Invalid note number.")

    elif position > len(notes):
        print("🤖 JARVIS: Note number doesn't exist.")

    else:
        notes[position - 1] = value
        print("🤖 JARVIS: Note updated.")

def clear_notes():
    notes.clear()
    print("🤖 JARVIS: Notes Cleared")

def save_notes():
    if not notes:
        print("🤖 JARVIS: No notes to save.")
        return
    
    with open("notes.json","w") as file :
        json.dump(notes, file)

    return("Notes saved successfully.")

def load_notes():
    with open("notes.json","r") as file:
        saved_notes = json.load(file)
        if not saved_notes:
            print("🤖 JARVIS: No notes saved yet")
            return

        notes.extend(saved_notes)
        print("🤖 JARVIS: ALL saved notes loaded!")


def run_command(operation,value):
    if operation == say_hello or operation == how_am_i :
        return f"🤖 JARVIS: {operation(value)}"
        
    else :
        return f"🤖 JARVIS: {operation()}"

commands = {
    "hello": say_hello,
    "how are you": how_am_i,
    "who are you": who_am_i,
    "time": current_time,
    "date": today_date,
    "age": calculate_age,
    "joke": joke,
    "memory": get_memory,
    "forget": delete_memory,
    "save": save_notes,
}
 
hello_responses = [
    "Hello!",
    "Hey!",
    "Hi there!",
    "Nice to see you!"
]

how_are_you_responses = [
    "I'm doing great",
    "I'm fine",
    "I'm doing good",
    "All systems are running"
]

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "Why did the programmer quit his job? Because he didn't get arrays! 😂",
    "Why was the JavaScript developer sad? Because he didn't know how to null his feelings. 😭",
    "Why do programmers hate nature? It has too many bugs! 🐛",
    "What do you call a programmer from Finland? Nerdic! 😄",
    "Why did the developer go broke? Because he used up all his cache! 💸",
    "How many programmers does it take to change a light bulb? None. It's a hardware problem! 😂",
    "A SQL query walks into a bar, walks up to two tables and asks... Can I join you? 🍺",
    "Why was the computer cold? It left its Windows open! 🪟",
    "What did the computer say when it got hungry? Let's get some bytes! 🍔"
]