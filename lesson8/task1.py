# Написати функцію. Є послідовність чисел - наприклад список, перевірити чи всі значення в
# ньому будуть унікальними(не повторюватись)

# [1, 2, 2, 3, 4, 2] -> {1, 2, 3, 4}
print([1, 2, 4])
print({1, 2, 4})


def check_unique(my_list: list) -> str:
    if len(my_list) > len(set(my_list)):
        return 'Є неунікальні значення'
    elif len(my_list) == len(set(my_list)):
        return 'Все ок!'


if __name__ == "__main__":
    print(check_unique([1, 2, 4]))