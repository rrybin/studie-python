""" def print_messages(): 

    def say_hello():
        print('Hello')

    def say_goodbye():
        print('Goodbye')

    say_hello()
    say_goodbye()
 """
#print_messages()

""" def main():
    say_hello()
    say_goodbye()

def say_hello():
    print('Hello')
"""
# def say_goodbye():
#     print('Goodbye')

# #main() 

# def say_hello(name):
#     print(f'Hello {name}')

# say_hello('Bob')
# say_hello('Anna')

# def print_person(age, name='Jack'):
#     if age > 120 or age < 1:
#         print('Invalid age')
#         return
#     print(f'Name: {name}, Age: {age}')

# print_person(37,'Tom')
# print_person(34)
# print_person(130, 'Bob')

# def sum(*numbers):
#     result = 0
#     for n in numbers:
#         result += n
#     print(f'sum = {result}')

# sum(1,2,3,4,5)
# sum(3,4,5,6,7)

# def double(number):
#     return 2 * number

# print(double(4))
# print(double(8))

# message = say_goodbye
# message()

# def do_operation(a,b,operation):
#     result = operation(a,b)
#     print(f'result = {result}')

# def sum(a,b):
#     return a + b

# def multiply(a,b):
#     return a * b

# do_operation(5,4,sum)
# do_operation(5,4,multiply)

# def subtrack(a,b):
#     return a - b

# def select_operation(choice):
#     if choice == 1:
#         return sum
#     elif choice == 2:
#         return subtrack
#     else:
#         return multiply

# operation=select_operation(1)
# print(operation(10,6))

# operation=select_operation(2)
# print(operation(10,6))

# operation=select_operation(3)
# print(operation(10,6))

# message = lambda: print('Hello')
# message()

# square = lambda n: n*n

# print(square(2))
# print(square(4))

# sum = lambda a,b: a + b
# print(sum(4,5))
# print(sum(5,6))

# def do_operation(a,b,operation):
#     result = operation(a,b)
#     print(f'result = {result}')

# do_operation(5,4, lambda a,b: a+b)
# do_operation(5,4, lambda a,b: a*b)
name = 'Tom'

def say_hi():
    global name 
    name = 'Anna'
    print(f'Hello, {name}')
    age = 32
    print(f'Age: {age}')

def say_bye():
    #name = 'Jim'
    print(f'Goodbye, {name}')
    age = 35
    print(f'Age: {age}')

say_hi()
say_bye()

def outer():
    n = 5

    def inner():
        nonlocal n
        n = 25
        print(n)

    inner()
    print(n)

outer()