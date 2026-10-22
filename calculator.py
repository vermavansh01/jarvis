history = []
last_calculation = []
calculation_count = 0
operation_count = {
    "add": 0,
    "subtract": 0,
    "multiply": 0,
    "divide": 0
}
redo_history = []

def view_history(num):
    if not history:
        print("\n🤖 JARVIS: No calculations yet.")
        return 

    print("\n🤖 JARVIS: Calculation History:")

    for item in history[-num:]:
        print(f"🤖 JARVIS: {item}")

def clear_history():
    history.clear()
    print("🤖 JARVIS: Calculation history cleared!")

def get_last():
    if not last_calculation:
            print("🤖 JARVIS: No calculations yet.")
            return 
    
    print(f"\n🤖 JARVIS: Last calculation: {last_calculation[0]}")

def get_count():
    print(f"You have performed {calculation_count} calculations.")

def set_operation_count(operation):
    operation_count[operation] += 1

def get_stats():
    print(f"🤖 JARVIS: Total calculations → {calculation_count}\nAdditions → {operation_count['add']}\nSubtractions → {operation_count['subtract']}\nMultiplications → {operation_count['multiply']}\nDivisions → {operation_count['divide']}")

def undo():
    if not history:
        print("\n🤖 JARVIS: Nothing to undo.")
        return

    removed = history.pop()
    redo_history.append(removed)
    print(f"\n🤖 JARVIS: Removed: {removed}")

def redo():
    if not redo_history:
        print("\n🤖 JARVIS: Nothing to redo.")
        return

    restored = redo_history.pop()
    history.append(restored)
    print(f"\n🤖 JARVIS: Restored: {restored}")

def add(num1,num2):
    return f"{num1} + {num2} : {num1 + num2}"

def subtract(num1,num2):
    return f"{num1} - {num2} : {num1 - num2}"

def multiply(num1,num2):
    return f"{num1} * {num2} : {num1 * num2}"

def divide(num1,num2):
    return f"{num1} / {num2} : {num1 / num2:.2f}"

def get_numbers():
    while True:
        try:
            print("\n🤖 JARVIS: Enter first number!")
            num1 = int(input("👤 You: "))

            print("\n🤖 JARVIS: Enter second number!")
            num2 = int(input("👤 You: ")) 

            return num1, num2 
        except ValueError:
            print("🤖 JARVIS: Please enter a valid integer")

def calculation(operation):
    global calculation_count
    while True:    
        try:  
            a, b = get_numbers()
            result = operation(a,b)
            history.append(result)
            last_calculation.clear()
            last_calculation.append(result)
            calculation_count += 1
            return f"\n🤖 JARVIS: {result}"
        
        except ZeroDivisionError:
            print("\n🤖 JARVIS: You can't divide by zero")
    
operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}

other_opeations = {
    "history clear": clear_history,
    "last": get_last,
    "stats": get_stats,
    "count": get_count,
    "undo": undo,
    "redo": redo
}
