# Введено число з клавіатури, знайти мінімальне та максимальне значення введеного числа,
# створити дві змінні поза циклом sum_min, sum_max -> знайти суму всіх чисел до мінімального
# та максимального числа використовуючи цикл for та діапазон range


max_numbers = max(3, 5, 8, 2)
min_numbers = min(3, 5, 8, 2)

sum_max = 0
sum_min = 0
for i in range(0, max_numbers + 1):
    sum_max += i  # 0, 1, 2, 3, 4, 5, 6, 7, 8 -> 36
for i in range(0, min_numbers + 1):
    sum_min += i  # 0, 1, 2 -> 3


print(sum_min)
print(sum_max)
