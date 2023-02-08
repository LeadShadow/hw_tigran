'''
Метод: sub
Дана строка символов.
Исключить из этой строки группы символов, расположенные между скобками [, ].
Сами скобки тоже должны быть исключены.
Пред
'''

import re


s = 'Забрати з цієї [групи] символів, [які розміщені між] дужками [, ]. []'

print(re.findall(r'\[.*?\]', s))


sanitize_string = re.sub(r'\[.*?\]', '', s)
print(sanitize_string)