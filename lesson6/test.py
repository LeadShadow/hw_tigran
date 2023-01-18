# (1, 3.2, 'string')
string = 'my string'
print(string[0])

my_tuple = tuple()
another_tuple = ()
print(my_tuple)
print(another_tuple)

not_empty = (1, 2, 3)
print(not_empty)
print(not_empty[0])
print(not_empty[1])
print(not_empty[2])

empty_dict = {}
another_dict = dict()
print(empty_dict)
print(another_dict)

some_dict = {
    'name': 'Oleksandr',
    1: 'one'
}
print(some_dict)

some_dict['key'] = 'dawda'
some_dict['new_key'] = 'new_value'
print(some_dict)

for i in not_empty:
    print(i)


for i in some_dict.values():
    print(i)
