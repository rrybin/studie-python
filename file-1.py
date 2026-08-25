if True:
    print('Hello')

#Comment

'''
Comment
Comment
'''
print('Full name:', 'Tom', 'Smith')

#name = input('Input name: ')
#print('Hello', name)

userName = 'Tom'
user_name = 'Jack'
print(userName, user_name)
userName = 4
print(userName)

isMarried = False
if isMarried:
    print(isMarried)
else:
    print(isMarried)
'''
userAge = input('How old are you? ')
if int(userAge) > 50:
    print('You are old')
else:
    print('You are young')
'''
#binary
a = 0b11
b = 0b1011
c = 0b100001
print(a,b,c)

#octa
a = 0o7
b = 0o11
c = 0o17
print(a,b,c)

#hex
a = 0x0A
b = 0xFF
c = 0xA1
print(a,b,c)

#float
height = 1.68
pi = 3.14
weight = 68.
print(height,pi,weight)

x = 3.9e3
print(x)
x = 3.9e-3
print(x)

#complex
complexNumber = 1+2j
print(complexNumber)

text = ('Row number one '
        'Row number two')
print(text)

text = '''Row number one 
Row number two'''
print(text)

path = 'C:\python\name'
print(path)
path = r'C:\python\name'
print(path)

userName = 'Bob'
userAge = 35
user = f'name: {userName} age: {userAge}'
print(user)

print(type(userName))
print(type(userAge))
print(7/2)
print(7//2)
print(7%2)

number = 5
print(f'number = {number:0b}')
while number > 0:
    print(f'number = {number}')
    number -= 1
else:
    print(f'number = {number}. Finish')

message = 'Hello'

for i in message:
    print(i)

for i in range(0, 10, 2):
    print(i, end=' ')
else:
    print('\nLoop is end')

i = 1
j = 1
while i < 10:
    while j < 10:
        print(i*j, end='\t')
        j += 1
    print('\n')
    j=1
    i += 1

number = 0
while number < 5:
    number +=1
    if number == 3:
        continue
    print(f'number = {number}')