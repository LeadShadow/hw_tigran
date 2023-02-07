# Напишите функцию parse_folder, она принимает единственный параметр path, который является
# объектом Path. Функция должна просканировать директорию path и вернуть кортеж из двух списков.
# Первый — это список файлов внутри директории, второй — список директорий.

# Пример вывода функции:

# (['.gitignore', 'readme.md'],
#  ['.git', '.idea', '.vscode', 'module-01', 'module-02', 'module-03', 'module-04', 'module-05',
#  'module-06', 'module-07',
#   'module-08', 'module-09', 'module-10', 'module-11', 'module-12'])
# ([назви файлів], [назви папок])
from pathlib import Path
p = Path('C:/Users/pc/Desktop/заняття/hw_tigran/lesson12')


def parse_folder(path: Path):
    files = []
    folders = []
    for el in path.iterdir():
        if el.is_file():
            files.append(el.name)
        else:
            folders.append(el.name)
    return files, folders


if __name__ == "__main__":
    print(parse_folder(p))