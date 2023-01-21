# hello.jpg, hello.docx, hello.txt, hello.py, hello.html


def check_expansion(param: str):
    if param.endswith('.jpg'):
        print('Це фото!')
    if param.endswith('.docx'):
        print('Це вордовський документ!')
    if param.endswith('.txt'):
        print('Це текстовий документ!')
    if param.endswith('.py'):
        print('Це пайтон файл!')
    if param.endswith('.html'):
        print('Це хтмл!')


check_expansion('hello.py')

