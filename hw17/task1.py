# мы решали задачу выплат по коммунальным платежам. Они представляли собой
# список payment с положительными и отрицательными значениями. Создайте функцию
# positive_values и с помощью функции filter отфильтруйте список payment по
# положительным значениям, и верните его из функции.
#
# payment = [100, -3, 400, 35, -100] -> [100, 400, 35]


def positive_values(list_payment):
    list1 = []
    for i in list_payment:
        if i > 0:
            list1.append(i)
    return list(filter(lambda sum: sum > 0, list_payment))


if __name__ == "__main__":
    print(positive_values([100, -3, 400, 35, -100]))