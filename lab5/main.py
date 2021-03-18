import operator
import collections
import os
import math
import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'

class Symbol(object):
    code = ''
    def __init__(self, arg, parg):
        self.a = arg
        self.p = parg

    def __repr__(self):
        return f'{repr(self.a)} - {str(self.p)} - {self.code}'

    def __lt__(self, other):
         return self.p < other.p

    def __add__(self, other):
        return Symbol('', self.p + other.p)
    
    def __sub__(self, other):
        return Symbol('', abs(self.p - other.p))

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)


def fano(l):
    if len(l) == 1:
        return

    n = min(enumerate([sum(l[:i]) - sum(l[i:]) for i in range(1, len(l))]), key=operator.itemgetter(1))[0] + 1

    for i, e in enumerate(l):
        e.code += ('0' if i < n else '1')

    fano(l[:n])
    fano(l[n:])


if __name__ == '__main__':
    cstep = int(sys.argv[1])

    for z, file in enumerate(['../lab1/f1.txt', '../lab1/f2.txt', '../lab2/eng.txt']):
        enc_file = f'{str(z)}.bin'
        print('File', file)
        with open(file, encoding="utf-8") as f:
            content = f.read()

        content = content.lower()
        content_tmp = ''
        for c in content:
            if c in alphabet:
                content_tmp += c
        content = content_tmp.replace(' ', '')
        content = content.replace('\n', '')

        counter = collections.defaultdict(int)
        for ci in range(0, len(content) - cstep + 1, cstep):
            counter[content[ci:ci+cstep]] += 1

        print(counter)

        p = {k: x / sum(counter.values()) for k, x in counter.items()}
        alp = [Symbol(x, y) for x, y in p.items()]
        fano(alp)

        #if len(alp) < 10:
        print('\n'.join(repr(x) for x in alp))
        
        # Encoding

        bits = ""

        for ci in range(0, len(content) - cstep + 1, cstep):
            for a in alp:
                if content[ci:ci+cstep] == a.a:
                    bits = bits + a.code


        #print(bits)

        if os.path.isfile(enc_file):
            os.remove(enc_file)

        with open(enc_file, 'w') as f:
            f.write(bits)

        # Decoding

        pass

        # Calc
        avg_len = sum(x.p * len(x.code) for x in alp)
        print('Средняя длина кодового слова -', avg_len)

        #with open(enc_file, 'ab') as f:
        #    entropy = -sum(x * math.log2(x) for x in p.values())
        #    print('Энтропия -', entropy)

        with open(enc_file, "r") as encoded:
            content = encoded.read()

        for step in range(1, 3 + 1):
            counter = collections.defaultdict(int)
            for cc in range(len(content) - step + 1):
                counter[content[cc:cc+step]] += 1

            print (counter)

            p = [x / len(content) for x in counter.values()]

            e = -sum(x * math.log2(x) for x in p) / step
            print('Step', step, '-', e)

            r = avg_len - e
            print('Избыточность кода -', r)

        print('Encoded to file', enc_file, '\n\n')
