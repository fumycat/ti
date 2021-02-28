from collections import defaultdict
from math import log2


def proc(file_name):
    print('File', file_name)
    with open(file_name) as file:
        content = file.read()

    total = len(content)

    for step in range(2, 5):
        counter = defaultdict(int)
        for cc in range(len(content) - step + 1):
            counter[content[cc:cc+step]] += 1

        p = [x / total for x in counter.values()]

        entropy = -sum(x * log2(x) for x in p) / step
        print('step', step, ' ', entropy)

    print()


if __name__ == '__main__':
    proc('f1.txt')
    proc('f2.txt')
