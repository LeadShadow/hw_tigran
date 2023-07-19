from collections import UserDict, UserList, UserString
import string
# cli -> command line interface
# class Tigran(Sasha, Oksana):
# color_eyes = 'green'
# color_eyes = 'brown'


class A:
    x = 'I am A class'


class B:
    x = 'I am B class'
    y = 'I exists only in B class'


class C(A, B):
    c = 'I exists only in C class'


c = C()
print(c.c)  # C
print(c.y)  # B
print(c.x)  # A


class ValueSearchableDict(UserDict):
    def has_in_values(self, value):
        return value in self.data.values()


as_dict = ValueSearchableDict()
as_dict['a'] = 1  # self.data = {'a': 1}
print(as_dict.has_in_values(1))


class CountableList(UserList):
    def sum(self):
        return sum(map(lambda x: int(x), self.data))

    def sum_1(self):
        result = 0
        for i in self.data:
            result += int(i)
        return result


countable = CountableList([1, '2', '3', 4, '5'])
countable.append(6)
print(countable.sum())
print(countable.sum_1())


class TruncatedString(UserString):
    max_len = 7
    def truncated(self):
        self.data = self.data.removeprefix('+').replace('(', '').replace(')', '').replace('-', '')


ts = TruncatedString('+38(093-731-(60-48)')
ts.truncated()
print(ts.data)


class NameTooShortError(Exception):
    pass


class NameStartsFromLowError(Exception):
    pass


def enter_name():
    name = input('Enter name: ')
    if len(name) < 2:
        raise NameTooShortError
    if name[0] not in string.ascii_uppercase:
        raise NameStartsFromLowError



while True:
    try:
        name = enter_name()
        break
    except NameTooShortError:
        print('Name is too short, need more than 2 symbols')
    except NameStartsFromLowError:
        print('Name should start from capital letter')