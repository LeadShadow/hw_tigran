# Создайте список years_list, содержащий год, в который вы родились, и каждый
# последующий год вплоть до вашего пятого дня рождения. Например, если вы
# родились в 1980 году, список будет выглядеть так: years_list = [1980, 1981,
# 1982, 1983, 1984, 1985]


year = int(input('Введіть свій рік народження: '))


def get_year(year: int) -> list:
    list_years = []
    for i in range(6):
        list_years.append(year + i)
    return list_years


years_list = (year + i for i in range(6))
print(*years_list)
print(get_year(year))

