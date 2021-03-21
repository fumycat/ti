from itertools import *
import operator

data = 'abcde'


for x, y in list(chain(*[list(product([x], range(x+1, len(data)))) for x in range(1, len(data)-1)])):
    print(data[:x], data[x:y], data[y:])

# ладно...

l = [0.6, 0.1, 0.1, 0.1, 0.1]
l.sort()
print(l)

# print([abs(sum(l[:x]) - sum(l[x:y])) + abs(sum(l[x:y]) - sum(l[y:])) for x, y in list(chain(*[list(product([x], range(x+1, len(l)))) for x in range(1, len(l)-1)]))])

xy_list = list(chain(*[list(product([x], range(x+1, len(l)))) for x in range(1, len(l)-1)]))

n = min(enumerate([abs(sum(l[:x]) - sum(l[x:y])) + abs(sum(l[x:y]) - sum(l[y:])) for x, y in xy_list]), key=operator.itemgetter(1))

print(n, xy_list[n[0]])
