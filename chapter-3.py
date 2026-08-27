class Person:
    def __init__(self):
        print('Create object Person')
        self.name = ''
        self.age = 0
    def say_hello(self):
        print('Hello')
    def display_info(self):
        print(f'Name: {self.name}, age: {self.age}')


tom = Person()
bob = Person()
tom.name = 'Tom'
tom.age = 32
tom.company = 'BTS'
tom.say_hello()
tom.display_info()

print(tom.name, tom.company)
