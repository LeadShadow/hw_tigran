name = input('Input your name: ')
age = int(input('Input your age: '))
driver_license = input('Do you have driver license?: ')

if driver_license == 'No':
    driver_license = False
elif driver_license == 'Yes':
    driver_license = True


if name and age >= 18 and driver_license:
    print('You can rent a car')
else:
    print("You can't rent a car")

ascii_a1 = ord('A')
ascii_a2 = ord('a')
print(ascii_a2 == ascii_a1)
