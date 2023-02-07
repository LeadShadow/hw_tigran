# 'r' -> відкриття на читання (значення за замовчуванням)
# 'w' -> відкриття на запис, зміст файла видаляється, якщо файлу не існує, створюється новий
# 'x' -> відкриття на запис, якщо такого файлу не існує, інакше помилка
# 'a' -> відкриття на дозапис інформація в кінець файлу
# 'b' -> відкриття в бінарному вигляді
# 't' -> відкриття в текстовому режимі (значення за замовчуванням)
# '+' -> відкриття на читання і запис

# open

file = open('rge.txt', 'w+')
file.write('Hello!')
file.seek(0)

first_two_symbols = file.read(2)
print(first_two_symbols)
file.close()


file = open('rge.txt', 'w')
file.write('Hello!fsgrdhfghmjkhgfnbdvscaxsxsdfghyjj')
file.close()

file = open('rge.txt', 'r')
all_file = file.read()
print(all_file)
file.close()


file = open('test.txt', 'w')
file.write('Hello Sasha!')
file.close()

file = open('test.txt', 'r')
while True:
    symbol = file.read(1)
    if len(symbol) == 0:
        break
    else:
        print(symbol)

file.close()


file = open('test.txt', 'w')
file.write('first line\nsecond line\nthird line')

file.close()

file = open('test.txt', 'r')
while True:
    line = file.readline()
    if not line:
        break
    print(line)

file.close()

file = open('test.txt', 'r', encoding='utf-8')
lines = file.readlines()
print(lines)

file.close()


with open('test.txt', 'w+', encoding='utf-8') as file:
    file.write('Sasha!')