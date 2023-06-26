from pathlib import Path
print(str(10))


class User:
    name = 'Sasha'
    age = 18


print(User.name)
print(User.age)


user1 = User()
print(user1.name)
print(user1.age)

user2 = User()
user2.name = 'Tigran'
user2.age = 17

print(user2.name)
print(user2.age)


class User:
    name = 'UserName'
    age = 15

    def say_name(self):
        print(f'Hi I am {self.name} and I am {self.age} years old.')

    def set_age(self, age):
        self.age = age


sasha = User()
sasha.name = 'Sasha'
sasha.say_name()

sasha.set_age(18)
sasha.say_name()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f'Hi! {self.name}'


p = Person('Oleksandr', 18)
print(p.greeting())

class Human:
    name = ''
    def voice(self):
        print(f'Hello! My name is {self.name}')


class Developer(Human):
    language = ''
    def make_some_code(self):
        print(f'{self.name} has language: {self.language}')


class PythonDeveloper(Developer):
    language = 'Python'


class JSDeveloper(Developer):
    language = 'JS'


p_dev = PythonDeveloper()
p_dev.name = 'Sasha'
p_dev.voice()
p_dev.make_some_code()
