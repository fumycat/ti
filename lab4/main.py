import operator
import collections
import struct


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
        print('File', file)
        with open(file, encoding="utf-8") as f:
            content = f.read()
        counter = collections.defaultdict(int)
        for c in content:
            counter[c] += 1

        p = {k: x / sum(counter.values()) for k, x in counter.items()}
        alp = [Symbol(x, y) for x, y in p.items()]
        fano(alp)

        print('\n'.join(repr(x) for x in alp))
        
        bits = content
        for s in alp:
            bits = bits.replace(s.a, s.code)

        with open(f'{str(z)}.bin', 'ab') as f:
            for chunk in [bits[i:i + 8] for i in range(0, len(bits), 8)]:
                f.write(struct.pack('i', int(chunk[::-1], 2)))

        

        print('Encoded to file', f'{str(z)}.bin', '\n')
