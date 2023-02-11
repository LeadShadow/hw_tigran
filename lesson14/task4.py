# Данные о пользователях лучше хранить в формате бинарных файлов. Поэтому вам необходимо создать
# функцию, которая будет записывать логин и пароль пользователя в файл.
#
# Реализуйте функцию save_credentials_users(path, users_info), которая сохраняет информацию о
# пользователях с паролями в бинарном файле.
#
# Где:
#
# path - путь к файлу.
# users_info - словарь вида {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}, где ключ — логин
# (username) пользователя, а значение — его пароль (password).
# Требования:
#
# Каждая строка файла должна иметь следующий вид "username:password". Такой формат записи используют
# при Базовой аутентификации.
# Откройте файл для записи и сохраните ключ и значение из словаря users_info в виде отдельной строки
# "username: password" для каждого элемента словаря users_info
from pathlib import Path
def save_credentials_users(path: Path, users_info: dict):
    with open(path, 'wb') as bfile:
        for username, password in users_info.items():
            bfile.write(f'{username}:{password}\n'.encode())


save_credentials_users('test_task4.bin', {'Sasha': 'abcd202020', 'Misha': 'tonerf1921'})