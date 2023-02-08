"""
Створення директорій pathlib
"""


from pathlib import Path

new_dir = Path('Temp')
new_dir.mkdir(exist_ok=True)
new_dir.rmdir()

new_dir = Path('test1/Test1/Temp')
new_dir.mkdir(exist_ok=True, parents=True)