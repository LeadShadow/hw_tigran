"""
defaultdict: Удобно если мы разбиваем на разные списки наборы телефонных операторов
"""
# завдання полягає в тому, щоб розбити телефонних операторів, по типу
#  phone_operator_numbers['Kyivstar'].append(number)
# 050, 095 -> Vodafone
# 067, 096 -> Kyivstar
# 063, 093 -> Lifecell
# інші номери додати до Unknown
from collections import defaultdict

phone_numbers = ['0509993636', '0679993636', '0959993636',
                 '0969993636', '0509993637', '0639993636', '0509993632', '0339993632']

phone_operator_numbers = defaultdict(list)

for pn in phone_numbers:
    if pn.startswith('050') or pn.startswith('095'):
        phone_operator_numbers['Vodafone'].append(pn)
    elif pn.startswith('067') or pn.startswith('096'):
        phone_operator_numbers['Kyivstar'].append(pn)
    elif pn.startswith('063') or pn.startswith('093'):
        phone_operator_numbers['Lifecell'].append(pn)
    else:
        phone_operator_numbers['Unknown'].append(pn)


print(phone_operator_numbers)