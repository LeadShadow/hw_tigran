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
