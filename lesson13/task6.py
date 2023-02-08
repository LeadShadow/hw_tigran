"""
Запис в файл pathlib
"""

from pathlib import Path

list_data = ['First line\n', 'Second line\n', 'Third line\n', 'Hi guys!']

folder = Path('Temp')
with open(folder / 'test.txt', 'w', encoding='utf-8') as file:
    for line in list_data:
        file.write(line)

with open(folder / 'test1.txt', 'w', encoding='utf-8') as file:
    file.writelines(list_data)