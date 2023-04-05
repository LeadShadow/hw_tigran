import random

print(random.randint(1, 1000))


print(random.random())

fruits = ['apple', 'banana', 'orange']
random.shuffle(fruits)
print(fruits)

print(random.choice(fruits))

print(random.choices(fruits, k=4))  # N кількість

try:
    winners = random.sample(fruits, k=4)
except ValueError:
    print('N кількість більша за довжину вибірки')
