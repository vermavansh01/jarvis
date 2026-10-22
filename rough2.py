# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return "Dog bark"
#     def spark(self):
#         return "Dog "
# dog = Dog()
# dog.speak()
# class Animal:
#     def speak(self):
#         print("Animal sound")


# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")


# class Cat(Animal):
#     def speak(self):
#         print("Cat meows")

# animals = [Dog(), Cat(), Dog(), Cat()]
# for animal in animals:
#     animal.speak()
# try:
#     number = int(input("Enter number: "))
# except ValueError:
#     print("Invalid number")
# else:
#     print("Number is valid")
# finally:
#     print("This always runs")
class InvalidAgeError(Exception):
    pass
while True :
    try:
        age = int(input("Enter your age: "))

        if age < 0 or age > 120 :
            raise InvalidAgeError("Invalid age")
        
        print("Valid age")

    except InvalidAgeError as e:
        print(f"Error: {e}")

    except ValueError :
        print(f"Error: Please enter a valid integer")

    else:
        break