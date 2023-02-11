# Pathlib
# .name, .parent, .is_dir(), .is_file(), .exists(), .unlink(), .suffix, .iterdir(), .glob()


from pathlib import Path

dir = Path('C:/Users/pc/Desktop/заняття/hw_tigran/lesson14')

for el in dir.glob('**/*.txt'):
    print(el)


