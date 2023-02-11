""""
Робота з файлами середовища pathlib
"""
# 101010101010010101
from pathlib import Path

filetext = Path('Test/my_text_file.txt')


filetext.write_text('First block\nSecond block\nThird block')
print(filetext.read_text())

file_bin = Path('Test/my_bin.bin')
file_bin.write_bytes(b'Binary data')
print(file_bin.read_bytes().decode())
