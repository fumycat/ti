from random import choices

alphabet = 'abcde'
weights1 = [0.2] * 5
weights2 = [0.1, 0.1, 0.1, 0.6, 0.1]
size = 10240

with open('f1.txt', 'w') as file:
    file.write(''.join(choices(alphabet, weights=weights1, k=size)))

with open('f2.txt', 'w') as file:
    file.write(''.join(choices(alphabet, weights=weights2, k=size)))

