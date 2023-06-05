from collections import UserDict, UserList, UserString
import string

class A:
    x = 'I am A class'


class B:
    x = 'I am B class'
    y = 'I exist only in B class'


class C(A, B):
    c = 'I exist only in C class'


c = C()
print(c.c)
print(c.y)
print(c.x)


# UserDict, UserList, UserString

# self.data -> {}
class ValueSearchDict(UserDict):
    def has_in_values(self, value):
        return value in self.data.values()


as_dict = ValueSearchDict()
as_dict['a'] = 1  # {'a': 1} -> as_dict - клас і словник 2 в 1
as_dict.has_in_values(1)
as_dict.has_in_values(2)


# [1, '2', 3, '4'] -> [1, 2, 3, 4]
class CountableList(UserList):
    def sum(self):
        return sum(map(lambda x: int(x), self.data))


countable = CountableList([1, '2', 3, '4'])
countable.append('5')
print(countable.sum())


class TruncatedString(UserString):
    MAX_LEN = 7

    def truncate(self):
        self.data = self.data[:self.MAX_LEN]


truncated = TruncatedString('Hello World')
print(truncated.data)
truncated.truncate()
print(truncated.data)


def input_number():
    num = 0
    while True:
        try:
            num = input('Enter integer number: ')
            return int(num)  # int('89'),   int('dwakakw')
        except ValueError:
            print(f'"{num}" is not a number, try again')


num = input_number()
print(num)


class NameTooShortError(Exception):
    pass


class NameStartsFromLowError(Exception):
    pass


def enter_name():
    name = input('Enter name: ')
    if len(name) < 3:
        raise NameTooShortError
    if name[0] not in string.ascii_uppercase:
        raise NameStartsFromLowError


while True:
    try:
        name = enter_name()
        break
    except NameTooShortError:
        print('Name is too short, need more than 3 symbols')
    except NameStartsFromLowError:
        print('Name should start from capital letter')