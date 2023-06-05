import collections
from pathlib import Path
from collections import namedtuple

way = Path('C:/Users/pc/Desktop/заняття/hw_tigran/lesson26')

print(way.name)
Person = namedtuple('Person', ['name', 'age'])

person = Person('Sasha', 18)
print(person.name)
print(person.age)


class User:
    name = 'Sasha'
    age = 18


user1 = User()
print(user1.name)
print(user1.age)

user2 = User()
user2.name = 'Tigran'
user2.age = 17

print(user2.name)
print(user2.age)


class User:
    name = 'Sasha'
    age = 18

    def say_name(self):
        print(f'Hi! I am {self.name} and I am {self.age} years old')

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name


maks = User()
maks.set_name('Maks')
maks.set_age(15)
maks.say_name()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f'Hi! {self.name}'


p = Person('Oleksandr', 18)
print(p.name)
print(p.age)
print(p.greeting())

print(10 + 10)


class Human:
    name = ''

    def voice(self):
        print(f'Hello! My name is {self.name}')


class Developer(Human):
    field_description = 'My Programming language'
    language = ''

    def make_some_code(self):
        return f'{self.field_description} is {self.language}'


class PythonDeveloper(Developer):
    language = 'Python'


class JsDeveloper(Developer):
    language = 'JS'


p_dev = PythonDeveloper()
p_dev.name = 'Sasha'
p_dev.voice()
print(p_dev.make_some_code())
