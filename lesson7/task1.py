# є випадковий список, потрібно представити його в зворотньому напрямку
# [1, 3, 5] -> [5, 3, 1]


def reverse_list(my_list: list) -> list:
    return my_list[::-1]


print(reverse_list([1, 3, 5]))
