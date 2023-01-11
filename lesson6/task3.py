# У нас есть кортеж показаний задолженностей по коммунальным услугам в конце месяца.
# Задолженности могут быть отрицательными — у нас переплата, или положительными, если
# необходимо оплатить по счетам. Напишите функцию amount_payment, которая принимает на вход
# список платежей, суммирует положительные значения и возвращает сумму платежа в конце месяца.


# -200 -> переплата
# 200 -> треба платити
def amount_payment(payment: tuple):
    sum = 0
    for i in payment:
        if i > 0:
            sum = sum + i
    return sum


if __name__ == "__main__":
    print(amount_payment((100, 500, 1000, -600, -400, 400)))
