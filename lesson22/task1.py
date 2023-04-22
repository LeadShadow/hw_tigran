# Задание
# Вам нужно реализовать полезную функцию для вывода списка коллег, которых надо
# поздравить с днём рождения на неделе.
#
# У вас есть список словарей users, каждый словарь в нём обязательно имеет ключи name
# и birthday. Такая структура представляет модель списка пользователей с их именами и
# днями рождения. name — это строка с именем пользователя, а birthday — это datetime
# объект, в котором записан день рождения.
#
# Ваша задача написать функцию get_birthdays_per_week, которая получает на вход список
# users и выводит в консоль (при помощи print) список пользователей, которых надо поздравить
# по дням.
#
# Условия приёмки
# get_birthdays_per_week выводит именинников в формате:
# Monday: Bill, Jill
# Friday: Kim, Jan
# Пользователей, у которых день рождения был на выходных, надо поздравить в понедельник.
# Для отладки удобно создать тестовый список users и заполнить его самостоятельно.
# Функция выводит пользователей с днями рождения на неделю вперед от текущего дня.
# Неделя начинается с понедельника.
from datetime import datetime, timedelta
users = [
    {
        'name': 'Sasha',
        'birthday': '2000-04-20'
    },
    {
        'name': 'Tigran',
        'birthday': '2000-04-21'
    }
]

def get_birthdays_per_week(users: list[dict]):
    result = {}
    date_now = datetime.now()
    for dc in users:
        birthday = dc.get('birthday', None)
        birthday = datetime.strptime(birthday, "%Y-%m-%d")
        other_birthday = birthday.replace(year=date_now.year)
        difference = other_birthday.date() - date_now.date()
        if timedelta(-1) <= difference <= timedelta(7):
            day = datetime.weekday(other_birthday)
            if day == 0 or day == 5 or day == 6:
                day_week = 'Monday'
            elif day == 1:
                day_week = 'Tuesday'
            elif day == 2:
                day_week = 'Wednesday'
            elif day == 3:
                day_week = 'Thursday'
            else:
                day_week = 'Friday'
            for k, v in dc.items():
                result.update({day_week: dc.get('name')})
    return result

def get_beauty_print(dict: dict):
    string = ''
    for k, v in dict.items():
        string += f'{k}: {v}' + '\n'
    return string

print(get_beauty_print(get_birthdays_per_week(users)))