# Часто вам нужно подсчитать количество элементов в некоторой последовательности.
# Для этого удобно воспользоваться словарем.
#
# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
# mark_counts = {}
# for mark in student_marks:
#     if mark in mark_counts:
#         mark_counts[mark] += 1
#     else:
#         mark_counts[mark] = 1
# print(mark_counts)  # {4: 4, 2: 2, 6: 3, 7: 2, 3: 2, 5: 2, 1: 3}
# Такая задача встречается достаточно часто, и чтобы не писать одни и те же 6 строк кода
# постоянно, в collections добавили специальный словарь Counter:
#
# import collections
#
# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(student_marks)
# print(mark_counts)  # Counter({4: 4, 6: 3, 1: 3, 2: 2, 7: 2, 3: 2, 5: 2})
# Но на этом полезные свойства Counter не заканчиваются. Он может вывести наиболее частые элементы:
#
# import collections
#
# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(student_marks)
# print(mark_counts.most_common(1))  # [(4, 4)]
# print(mark_counts.most_common(2))  # [(4, 4), (6, 3)]
# Ещё Counter может отнять количество элементов одного Counter от другого поэлементно:
# from collections import Counter
#
# c = Counter(a=4, b=2, c=0, d=-2)
# d = Counter(a=1, b=2, c=3, d=4)
# c.subtract(d)
# print(c)  # Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
# Задание
# Есть список IP адресов:
IP = [
    "85.157.172.253",
    '85.157.172.233',
    '85.157.172.233',
    '65.157.172.253',
    '65.157.172.253',
    '65.157.172.253',
    '65.157.172.253'
]
# Реализуйте две функции. Первая get_count_visits_from_ip с помощью Counter будет возвращать
# словарь, где ключ — это IP, а значение — количество вхождений в указанный список.
# Пример:
# {
#     '85.157.172.253': 2,
#     ...
# }
# Вторая функция get_frequent_visit_from_ip возвращает кортеж с наиболее часто встречаемым в списке
# IP и количеством его вхождений в список.
# Пример:
# ('66.50.38.43', 4)

from collections import Counter


def get_count_visits_from_ip(ips):
    return Counter(ips)

def get_frequent_visit_from_ip(ips):
    return Counter(ips).most_common(1)[0]


if __name__ == "__main__":
    print(get_count_visits_from_ip(IP))
    print(get_frequent_visit_from_ip(IP))