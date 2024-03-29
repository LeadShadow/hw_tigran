'''
. - один любой символ,кроме строки \n
? - 0 или 1 вхождение шаблона слева
+ - 1 и более вхождений шаблона слева
* - 0 и более вхождений шаблона слева
\w - любая цифра или буква [a-zA-Z0-9_] (\W - все, кроме буквы или цифры [^a-zA-Z0-9_])
\d - любая цифра [0-9] (\D - все, кроме цифры [^0-9])
\s - любой пробельный символ [\t\n\r\f\v] (\S - все, кроме не пробельного символа [^\t\n\r\f\v])
\b - граница слова
[..] - один из символов в скобках ([^..] - любой символ, кроме тех, что в скобках)
\ - экранирование спец.символов (пример: \. - означает точку или \+ - знак "плюс")
^ и $ - начало и конец строки соответственно
{n,m} - от n до m вхождений (пример: {,m} - от 0 до m)
a|b - соответствует a или b
() - группирует выражение и возвращает найденный текст
\t, \n, \r - символ табуляции, новой строки и возврат каретки
'''

'''
Метод: search
'''

import re

string = "Нильс Бор родился в семье профессора физиологии Копенгагенского университета Христиана Бора (1858—1911), " \
         "дважды становившегося кандидатом на Нобелевскую премию по физиологии и медицине[10], и Эллен Адлер (" \
         "1860—1930), дочери влиятельного и весьма состоятельного еврейского банкира и парламентария-либерала Давида " \
         "Баруха Адлера (дат. David Baruch Adler; 1826—1878) и Дженни Рафаэль (1830—1902) из британской еврейской " \
         "банкирской династии Raphael Raphael & sons[en][11]. Родители Бора поженились в 1881 году."


pattern = r'\d+'
result = re.search(pattern, string)
print(result)
f, l = result.span()
print(f, l)
print(string[f: l])
print(result.group())
