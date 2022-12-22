val = 'a'  # 10 -> str
try:
    val = int(val)  # 10 -> int
    print(val > 0)
except ValueError:
    print(f'val {val} is not a number')
finally:
    print('This will be printed')


age = input('How old are you?: ')
try:
    age = int(age)
    if age >= 18:
        print('You are adult')
    else:
        print('You are infant yet!')
except ValueError:
    print(f'{age} is not a number')
