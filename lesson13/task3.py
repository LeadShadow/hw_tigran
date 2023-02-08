# # Приклад 1
# # Наступна програма зчитує весь вміст файлу input.txt, записує його в змінну s,
# а потім виводить її в файл output.txt.
# Нехай в файл input.txt записано We are learning Python programming language

f1 = open('input.txt', 'r', encoding='utf-8')
f2 = open('output.txt', 'w')
s = f1.read()
f2.write(s)
f1.close()
f2.close()

