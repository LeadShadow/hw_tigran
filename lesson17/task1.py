# Дальше пойдут задачи на повторение и закрепление материала. Можно использовать любые техники,
# с которыми вы столкнулись в процессе обучения. И начнем мы с функций.
#
# В Python существует строковая функция isdigit(). Эта функция возвращает True,
# если все символы в строке являются цифрами, и есть по крайней мере один символ,
# иначе — False. Напишите функцию с именем is_integer, которая будет расширять
# функциональность isdigit(). При проверке строки необходимо игнорировать ведущие и
# замыкающие пробелы в строке. После исключения лишних пробелов строка считается представляющей
# целое число, если:
#
# ее длина больше или равна одному символу
# она целиком состоит из цифр
# предусмотреть исключение, что, возможно, есть ведущий знак «+» или «-», после которого должны идти цифры
# тернарний оператор -> return True if s.isdigit() else False

# '100' -> '320d'.isdigit() -> False


def is_integer(s: str) -> bool:
    s1 = s.strip()   # '     +380    ' -> '+380'
    if len(s1) == 0:
        return False
    if s1[0] == '-' or s1[0] == '+':
        s2 = s1[1:]   # '+380' [1:] -> '380'
    return s2.isdigit()


if __name__ == "__main__":
    print(is_integer('     +380d    '))
