# Дан список целых чисел, найдите то, которое встречается нечетное количество раз.
# Всегда будет только одно целое число, которое встречается нечетное количество раз.
# [1, 2, 2, 2, 1]
import collections

temperatures = [1, 2, 2, 2, 1]

count = collections.Counter(temperatures)
print(count)

