# Потрібно перевірити чи тут є український номер
list_of_numbers = ['+380937316048', '+6473284328', '+380937316047']


def check_number(my_list: list):
    for i in my_list:
        if i.startswith('+380'):
            print('Є укр номер!')


check_number(list_of_numbers)