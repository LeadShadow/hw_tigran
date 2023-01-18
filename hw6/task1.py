# Написати функцію useless(list) де параметр list буде випадковий список
# Знайти в цьому списку максимальне значення і розділити його на довжину списка


# [1, 2, 4, 6, 8, 5, 4, 10]
def useless(my_list: list):
    max_ = 0
    for i in my_list:
        if i > max_:
            max_ = i
    return max_ / len(my_list)


if __name__ == "__main__":
    print(useless([1, 2, 4, 6, 8, 5, 4, 16]))


