# Задание
# Напишите консольного бота помощника, который будет распознавать команды, вводимые
# с клавиатуры, и отвечать согласно введенной команде.
#
# Бот помощник должен стать для нас прототипом приложения-ассистента. Приложение-ассистент
# в первом приближении должен уметь работать с книгой контактов и календарем. В этой домашней
# работе сосредоточимся на интерфейсе самого бота. Наиболее простой и удобный на начальном
# этапе разработки интерфейс - это консольное приложение CLI (Command Line Interface).
# CLI достаточно просто реализовать. Любой CLI состоит из трех основных элементов:
#
# Парсер команд. Часть, которая отвечает за разбор введенных пользователем строк, выделение
# из строки ключевых слов и модификаторов команд.
# Функции обработчики команд — набор функций, которые ещё называют handler, они отвечают
# за непосредственное выполнение команд.
# Цикл запрос-ответ. Эта часть приложения отвечает за получение от пользователя данных и
# возврат пользователю ответа от функции-handlerа.
# На первом этапе наш бот-ассистент должен уметь сохранять имя и номер телефона, находить
# номер телефона по имени, изменять записанный номер телефона, выводить в консоль все записи,
# которые сохранил. Чтобы реализовать такую несложную логику, воспользуемся словарем.
# В словаре будем хранить имя пользователя как ключ и номер телефона как значение.
#
# Условия#
# Бот должен находиться в бесконечном цикле, ожидая команды пользователя.
# Бот завершает свою работу, если встречает слова: .
# Бот не чувствительный к регистру вводимых команд.
# Бот принимает команды:
# "hello", отвечает в консоль "How can I help you?"
# "add ...". По этой команде бот сохраняет в памяти (в словаре например) новый контакт.
# Вместо ... пользователь вводит имя и номер телефона, обязательно через пробел.
# "change ..." По этой команде бот сохраняет в памяти новый номер телефона для существующего
# контакта. Вместо ... пользователь вводит имя и номер телефона, обязательно через пробел.
# "phone ...." По этой команде бот выводит в консоль номер телефона для указанного контакта.
# Вместо ... пользователь вводит имя контакта, чей номер нужно показать.
# "show all". По этой команде бот выводит все сохраненные контакты с номерами телефонов в консоль.
# "good bye", "close", "exit" по любой из этих команд бот завершает свою роботу после того,
# как выведет в консоль "Good bye!".
# Все ошибки пользовательского ввода должны обрабатываться при помощи декоратора input_error.
# Этот декоратор отвечает за возврат пользователю сообщений вида "Enter user name",
# "Give me name and phone please" и т.п. Декоратор input_error должен обрабатывать исключения,
# которые возникают в функциях-handler (KeyError, ValueError, IndexError) и возвращать
# соответствующий ответ пользователю.
# Логика команд реализована в отдельных функциях и эти функции принимают на вход одну или
# несколько строк и возвращают строку.
# Вся логика взаимодействия с пользователем реализована в функции main, все print и input
# происходят только там.
from lesson28.verify_phone import verify_phone
from decorator import input_error

def hello(*args):
    return 'Hello! How can I help you?'


# (Sasha, +380937316048)
@input_error
def add_contact(contacts, *args):
    name, phone = args[0], args[1]
    phone = verify_phone(phone)
    contacts[name] = phone
    return f'Added user {name}'


@input_error
def change_contact(contacts, *args):
    name, phone = args[0], args[1]
    phone = verify_phone(phone)
    contacts[name] = phone
    return f'Change user {name}'


@input_error
def show_phone(contacts, *args):
    name = args[0]
    return f'User - {name}, phone - {contacts[name]}'


def show_all(contacts, *args):
    result = 'List of all users: '
    for name, phone in contacts.items():
        result += '\n|User - {:^10}| phone - {:^15}'.format(name, phone)
    return result


def goodbye(*args):
    return None


def help_me(*args):
    return """Command format:
help or ? - help
hello - func of greeting
add <name> <phone> - add user to dict
change <name> <new_phone> - change the user's phone
phone <name> - show the user's phone number
show all - show all contacts
close or . or exit or stop - exit the program"""