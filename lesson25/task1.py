# Есть список name с именами пользователей, но все начинаются со строчной буквы.
#
# name = ["dan", "jane", "steve", "mike"]
# Разработайте функцию normal_name, которая принимает список имен и возвращает тоже список имен,
# но уже с правильными именами с заглавной буквы.
#
# ['Dan', 'Jane', 'Steve', 'Mike']
# Необходимо использовать функцию map. Не забудьте, что необходимо выполнить преобразование типов
# для map.



if __name__ == '__main__':
    print(list(map(str.title, ["dan", "jane", "steve", "mike"])))