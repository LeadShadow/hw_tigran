"""
Читаємо файл за допомогою бібліотеки Pathlib
"""

from pathlib import Path

folder = Path('Temp')
filename = folder / 'my.txt'

try:
    with open(filename, 'r', encoding='utf-8') as fh:
        print(fh.read())
except OSError:
    print(OSError)

print('hello world')
print('hello world')
print('hello world')
print('hello world')
print('hello world')