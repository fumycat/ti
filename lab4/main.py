import operator
import collections
import os
import math

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
    for z, file in enumerate(['../lab1/f1.txt', '../lab1/f2.txt', '../lab2/eng.txt']):
        enc_file = f'{str(z)}.bin'
        print('File', file)
        with open(file, encoding="utf-8") as f:
            content = f.read()
        counter = collections.defaultdict(int)
        for c in content:
            counter[c] += 1

        p = {k: x / sum(counter.values()) for k, x in counter.items()}
        alp = [Symbol(x, y) for x, y in p.items()]
        fano(alp)

        if len(alp) < 10:
            print('\n'.join(repr(x) for x in alp))
        
        # Encoding

        bits = content
        for s in alp:
            bits = bits.replace(s.a, s.code)

        if os.path.isfile(enc_file):
            os.remove(enc_file)

        with open(enc_file, 'ab') as f:
            for chunk in [bits[i:i + 8] for i in range(0, len(bits), 8)]:
                f.write(int(chunk[::-1], 2).to_bytes(1, 'little'))

        # Decoding

        pass

        # Calc

        avg_len = sum(x.p * len(x.code) for x in alp)
        print('Средняя длина кодового слова -', avg_len)

        entropy = -sum(x * math.log2(x) for x in p.values())
        print('Энтропия -', entropy)

        for step in range(2, 3 + 1):
            counter = collections.defaultdict(int)
            for cc in range(len(content) - step + 1):
                counter[content[cc:cc+step]] += 1

            p = [x / len(content) for x in counter.values()]

            e = -sum(x * math.log2(x) for x in p) / step
            print('Step', step, '-', e)

        r = avg_len - entropy
        print('Избыточность кода -', r)

        print('Encoded to file', enc_file, '\n\n')
