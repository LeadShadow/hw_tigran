# zip tar gz

import shutil

# make_archive('name', 'format', 'path') -> упакувати папку в якій ми працюємо в архів
archive_name = shutil.make_archive('backup', 'zip', 'dist')
shutil.unpack_archive(archive_name)
