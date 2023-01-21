hello_world = 'hello world'
print(hello_world[0])
print(hello_world[-1])

hello_world1 = 'f' + hello_world[1:]
print(hello_world1)
s = 'Hello'
s1 = s.upper()
print(s1)
print(s1.lower())
s = 'Sasha Samus'
print(s.startswith('sa'))  # True
s = 'hello.jpg'
print(s.endswith('jpg'))

# in
password = 'qwerty123'
if 'qwerty' in password or '123' in password:
    print('This password is incorrect!')


numbers = {2, 3, 5, 7, 10, 11, 30}
is_prime = 4 in numbers
print(is_prime)

user = {
    'name': 'Sasha',
    'surname': 'Samus',
    'age': 18
}

if 'age' in user:
    print(f'User is {user["age"]} years old')


password = input('Input password: ')
if len(password) < 8:
    print('Your password is too short')


