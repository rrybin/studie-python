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
# name = 'Tom'

# def say_hi():
#     global name 
#     name = 'Anna'
#     print(f'Hello, {name}')
#     age = 32
#     print(f'Age: {age}')

# def say_bye():
#     #name = 'Jim'
#     print(f'Goodbye, {name}')
#     age = 35
#     print(f'Age: {age}')

# say_hi()
# say_bye()

# def outer():
#     n = 5

#     def inner():
#         nonlocal n
#         n += 1
#         print(n)

#     return inner
    
# fn = outer()
# fn()
# fn()
# fn()

# def multiply(n):
#     def inner(m): return n*m

#     return inner

# fn = multiply(5)
# print(fn(5))
# print(fn(6))
# print(fn(7))

# def select(input_func):
#     def output_func():
#         print('*****************')
#         input_func()
#         print('*****************')
#     return output_func

# @select
# def hello():
#     print('Hello test')

# hello()

# def changecase(func):
#     def myinner():
#         return func().upper()
#     return myinner

# @changecase
# def myfunction():
#     return 'Hello Anna'

# print(myfunction())

# def null_decorator(func):
#     return func

# def uppercase(func):
#     def wrapper():
#         original_result = func()
#         modified_result = original_result.upper()
#         return modified_result
#     return wrapper

# @uppercase
# def greet():
#     return 'Hello, decorator!!!'

# print(greet())

# def check(input_func):
#     def output_func(*args):
#         name = args[0]
#         age = args[1]
#         age = 40
#         input_func(name.upper(),age)
#     return output_func

# @check
# def print_person(name, age):
#     print(f'Name: {name} Age: {age}')

# print_person('Anna', 32)

def check(input_func):
    def output_func(*args):
        result = input_func(*args)
        if result < 0:
            result = 0
        return result
    return output_func

@check
def sum(a,b):
    return a+b

result1 = sum(10, 20)
print(result1)

result2 = sum(10, -20)
print(result2)