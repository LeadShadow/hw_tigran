import re


s = 'I am 18 years old'
age = re.search(r'\d+', s)
print(age.group())

s = 'I bought 7 nuts for 6$ and 10 bolts for 3$'
numbers = re.findall(r'\d+', s)
print(numbers)

s = 'blue socks and red shoes'
pattern = r'(blue|white|red)'
p = re.sub(pattern, 'colour', s)
print(p)


