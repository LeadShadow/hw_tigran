'''
Метод: sub
'''

import re

s = 'The best language is java'

p = re.sub(r'Java|java', 'Python', s)
print(p)
