# operations = ["add", "divide", "add", "multiply", "divide"]
# sets = set(operations)
# # print(sets)
# a = {"python", "javascript", "react"}
# b = {"python", "java", "react"}
# print(a & b)
# print(a)
# print(a | b)
# print(a - b)
# numbers = [1, 2, 3, 4, 5]
# # sqaures = [i * i for i in numbers]
# # print(sqaures)
# # odd = [ i for i in numbers if i%2 == 1]
# # print(odd)
# # odd_squares = [ i * i for i in numbers if i%2 == 1]
# # print(odd_squares)
# # even_dict = {i: i * i for i in numbers if i%2 == 0}
# # print(even_dict)
# # squares = {i * i for i in numbers}
# # print(squares)
# result = ["even" if i % 2 == 0 else "odd" for i in numbers]
# print(result)
# add = lambda a, b: a + b
# print(add(1,2))
# numbers = [1, 2, 3, 4, 5]
# squares = list(map(lambda x: x * 10, numbers))
# print(squares)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd = list(filter(lambda x: x % 2 == 1, numbers))
# print(odd)
# names = ["Vansh", "Aman", "Christopher", "Raj", "Mohit"]
# result = sorted(names, key=lambda x: len(x), reverse=True)
# print(result)
# def add(*args):
#     return sum(args)
# print(add(10, 20, 30))
# def user_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} → {value}")

# user_info(name="Vansh", role="Developer", language="Python")
# def info(*args, **kwargs):
#     print(args)
#     print(kwargs)

# info(10, 20, 30, name="Vansh", role="Developer")
# def outer():
#     x = 10

#     def inner():
#         nonlocal x
#         x = 20

#     inner()
#     print(x)

# outer()
# class Student:
#     school = "ABC School"
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         return f"Hi, I am {self.name} and I am {self.age} years old."
    
#     @classmethod
#     def change_school(cls,new_school):
#         cls.school = new_school

#     @staticmethod
#     def is_valid_age(age):
#         return age >= 5

# student1 = Student("Vansh", 20)
# student2 = Student("Rahul", 25)
# Student.change_school("XYZ School")
# print(student1.name)
# print(student1.school)

# print(student2.name)
# print(student2.school)
# print(Student.is_valid_age(10))
# print(Student.is_valid_age(5))
# print(Student.is_valid_age(20))
# print(Student.is_valid_age(4))
# class Animal:
#     def speak(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def speak(self):
#         print("Dog bark")
#         super().speak()

# class Cat(Animal):
#     def speak(self):
#         print("Cats meow")
#         super().speak()

# animal = Animal()
# animal.speak()
# dog = Dog()
# dog.speak()
# cat = Cat()
# cat.speak()
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,value):
        if value > 0:
            self.__balance = value
        else:
            print("Invalid deposit amount")

account = BankAccount(5000)
account.balance = 70000
print(account.balance)

