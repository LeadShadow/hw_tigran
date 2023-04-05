person = ('Sasha', 'Nitch', 35, 'Boston', '0110')

import collections

Person = collections.namedtuple('Person', ['name', 'last_name', 'age', 'place', 'index'])

person = Person('Sasha', 'Samus', 19, 'Boston', '0110')
print(person.name)
print(person.last_name)
print(person.age)
print(person.place)
print(person[3])


class Person:
    name = 'Sasha'
    last_name = 'Samus'

print(Person.name)


student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 7, 8, 1, 2]
mark_counts = {}
for mark in student_marks:
    if mark in mark_counts:
        mark_counts[mark] += 1
    else:
        mark_counts[mark] = 1

print(mark_counts)

mark_counts = collections.Counter(student_marks)
print(mark_counts)

print(mark_counts.most_common(1))
print(mark_counts.most_common(2))


c = collections.Counter(a=4, b=2, c=0, d=-2)
d = collections.Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)

words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'orange']
grouped_words = {}

for word in words:
    char = word[0]
    if char not in grouped_words:
        grouped_words[char] = []   # 'a': []
    grouped_words[char].append(word)

print(grouped_words)



grouped_words = collections.defaultdict(list)

for word in words:
    char = word[0]
    grouped_words[char].append(word)

print(grouped_words)


d = collections.deque()
d.append('last')
d.appendleft('first')
d.insert(1, 'middle')
print(d)

print(d.pop())
print(d.popleft())
print(d)

d = collections.deque(maxlen=5)
for i in range(10):
    d.append(i)

print(d)


# comprehensions

sq = []
for i in range(1, 6):
    sq.append(i ** 2)

print(sq)

# Sorry baby
# Say it 1000 times
# class Sorry {
#    public static void main(String[] args) {
#        int x;
#        for(x=0, x<= 1000; x++){
#        System.out.println('Sorry Baby');
# }
# }
# }
user_input = int(input('Enter your number: '))
numbers = [i for i in range(1, user_input + 1)]
print(numbers)

sq = [i ** 2 for i in range(1, user_input+1)]
print(sq)


numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i ** 2 for i in numbers}
print(sq)

numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i: i ** 2 for i in numbers}
print(sq)