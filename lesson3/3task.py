# Вернемся снова к нашей предыдущей задаче.

# Напишите два двойных цикла. В первом цикле while мы постоянно запрашиваем целое число, а
# во втором с помощью цикла for считаем сумму четных чисел от 0 до введенного числа.
# Выход из первого цикла осуществляем, если ввели число 0, с помощью оператора break.

# Тесты используют две тестовые последовательности чисел:
#
# 10, 13, 73, 0 и ожидают сумму 1404
# 1, 2, 3, 4, 0 и ожидают сумму 10

sum = 0
while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
    for i in range(num + 1):
        if

        sum = sum + i