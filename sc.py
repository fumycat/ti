from collections import defaultdict
from math import log2

# '%.3f'

counter1 = defaultdict(int)
counter2 = defaultdict(int)

with open('f1.txt') as file:
    for c in file.read():
        counter1[c] += 1

with open('f2.txt') as file:
    for c in file.read():
        counter2[c] += 1

p1 = {k: x / sum(counter1.values()) for k, x in counter1.items()}
p2 = {k: x / sum(counter2.values()) for k, x in counter2.items()}

print('file 1:')
# print(counter1.items())
# print('Вероятности', p1)
print('Энтропия', -sum(x * log2(x) for x in p1.values()))

print()

print('file 2:')
# print(counter2.items())
# print('Вероятности', p2)
print('Энтропия', -sum(x * log2(x) for x in p2.values()))
