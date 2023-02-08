# Виберіть будь-яку папку на своєму пк, яка має вложенні директорії. Вивести на прінт
# в термінал її зміст

from pathlib import Path

p = Path('C:/Users/pc/Desktop/заняття/hw_tigran/lesson13')

def parse_file(path: Path):
    for el in path.iterdir():
        if el.is_dir():
            parse_file(el)
        else:
            print(f'This is file: {el.name}')


if __name__ == "__main__":
    parse_file(p)

