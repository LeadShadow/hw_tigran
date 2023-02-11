"""
Читаємо файл за допомогою бібліотеки Pathlib
"""

from pathlib import Path

folder = Path('Temp')
filename = folder / 'my.txt'

try:
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
except OSError as err:  # OSError -> err
    print(f'Помилка доступу до файлу: {err}')
finally:
    print('')
    print('\nОперація закінчилась')
