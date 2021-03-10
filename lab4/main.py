import operator

class Symbol(object):
    code = ''
    def __init__(self, arg, parg):
        self.a = arg
        self.p = parg


    def __repr__(self):
        return f'{self.a} - {str(self.p)} - {self.code}'

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

inp = {
    'a': 0.36,
    'b': 0.18,
    'c': 0.18,
    'd': 0.12,
    'e': 0.09,
    'f': 0.07,
}

alp = [Symbol(x, y) for x, y in inp.items()]

# print(alp)

def fano(l):
    if len(l) == 1:
        return
    # print('call', l)

    n = min(enumerate([sum(l[:i]) - sum(l[i:]) for i in range(1, len(l))]), key=operator.itemgetter(1))[0] + 1

    for i, e in enumerate(l):
        e.code += ('0' if i < n else '1')

    fano(l[:n])
    fano(l[n:])

fano(alp)

print('\n'.join(str(x) for x in alp))
