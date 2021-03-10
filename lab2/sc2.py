from collections import defaultdict
from math import log2
import sys

alp = 'abcdefghijklmnopqrstuvwxyz'

def proc(file_name):
	print('File', file_name)
	with open(file_name, encoding="utf-8") as file:
		content = file.read()

	content = content.lower()
	content_tmp = ''
	for c in content:
		if c in alp:
			content_tmp += c
	content = content_tmp.replace(' ', '')
	content = content.replace('\n', '')

	#print(content)

	total = len(content)
	last_e = 0
	for step in range(1, 150):
		counter = defaultdict(int)
		for cc in range(len(content) - step + 1):
			counter[content[cc:cc+step]] += 1

		p = [x / total for x in counter.values()]

		entropy = -sum(x * log2(x) for x in p) / step
		print('step', step, ' ', entropy)
		if abs(last_e - entropy) < 0.25:
			break
		last_e = entropy

	print()


if __name__ == '__main__':
	#proc('f1.txt')
	#proc('f2.txt')
	#proc('eng.txt')
	for arg in sys.argv[1:]:
		proc(arg)