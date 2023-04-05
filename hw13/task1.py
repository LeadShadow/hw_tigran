# Створити функцію get_days_from_birthday(date: datetime). Використовуючи модуль datetime,
# знайти кількість днів від вашої дати народження до теперішньої дати
from datetime import datetime
def get_days_from_birthday(date: datetime):
    date_day_of_birthday = datetime(year=2006, month=1, day=7)
    return (date - date_day_of_birthday).days


print(get_days_from_birthday(datetime.now()))