string1 = 'Hi'
string2 = "Hi"

string_will = """Як умру, то поховайте
Мене на могилі
Серед степу широкого
На Вкраїні милій,
Щоб лани широкополі,
І Дніпро, і кручі
Було видно, було чути,
Як реве ревучий.
Як понесе з України
У синєє море
Кров ворожу... отойді я
І лани і гори —
Все покину, і полину
До самого Бога
Молитися... а до того
Я не знаю Бога.
Поховайте та вставайте,
Кайдани порвіте
І вражою злою кров’ю
Волю окропіте.
І мене в сем’ї великій,
В сем’ї вольній, новій,
Не забудьте пом’янути
Незлим тихим словом."""

print(string_will)
print("spam " "eggs" == "spam eggs")

# \n -> перенос рядка
# \f -> перенос сторінки
# \r -> повернення каретки
# \t -> горизантальна табуляція
# \v -> вертикальна табуляція

s = 'Hi there!'

start = 0
end = 7

print(s.index('i'))
print(s.find('i', start, end)) # 5
print(s.find('q'))

print(s.rfind('e'))
print(s.rfind('e'))

s1 = 'I am learning strings in Python.Some new methods got now'
sentences = s1.split('.') # -> ['I am learning strings in Python', 'Some new methods got now']
print(sentences)

text = '. '.join(sentences)
print(text)

clean = '  some  '.strip()
print('  some  ')
print(clean)

dogs_text = 'All dogs bark like dogs.'
cats_text = dogs_text.replace('dogs', 'cats')
print(cats_text)

test_string1 = 'TestHook'.removeprefix('Test')
print(test_string1)

test_string2 = 'TestHook'.removeprefix('Hook')
print(test_string2)

test_string3 = 'TestHook'.removesuffix('Hook')
print(test_string3)

test_string4 = 'TestHook'.removesuffix('Test')
print(test_string4)


for i in range(16):
    s = 'int: {0:d}; hex: {0:x}; oct: {0:o}; bin: {0:b}'.format(i)
    print(s)


# f'{a}' -> '{}'.format(i)
a = 10
print(f'{a}')
print('{}'.format(a))


for num in range(12):
    # print(num, num ** 2, num ** 3)
    print('{:^12} {:^12} {:^12}'.format(num, num ** 2, num ** 3))
