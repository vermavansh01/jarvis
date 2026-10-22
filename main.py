import datetime as time
print('🤖 JARVIS: Hello! What is your name?')

name = input('👤 You: ')
while name == '':
        name = input("🤖 JARVIS: Enter your name!")

print(f'🤖 JARVIS: Nice to meet you, {name}!')
# print('🤖 JARVIS: How are you?')
# feeling = input('👤 You: ')

# while feeling == '':
#     print('🤖 JARVIS: How are you?')
#     feeling = input('👤 You: ')

# print("🤖 JARVIS: That's great")

while True:
      command = input("👤 You: ")

      if(command.lower() == "hello"):
            print (f"🤖 JARVIS: Hello {name}!")

      elif command.lower() == "exit" :
            print (f"🤖 JARVIS: Goodbye {name}")
            break
      elif command.lower() == "time":
            print (f"🤖 JARVIS: The current time is {time.datetime.now().strftime('%H:%M:%S')}")
            
      else:
            print ("🤖 JARVIS: I don't understand that yet")