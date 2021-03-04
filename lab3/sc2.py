from collections import defaultdict
from math import log2
import sys
import string

alp = string.printable

def proc(file_name):
	print('File', file_name)
	with open(file_name, encoding="utf-8") as file:
		content = file.read()

	content_tmp = ""
	text_flag = 0
	comment_flag = 0
	for c in content:
		if (comment_flag and c != '\n'):
			continue
		elif (text_flag == 1 and c != '"'):
			continue
		elif (text_flag == 2 and c != "'"):
			continue
		elif (c in alp):
			content_tmp += c
			if text_flag == 0:
				if c == '"':
					text_flag = 1
				if c == "'":
					text_flag = 2
			else:
				text_flag = 0
			if comment_flag == 0:
				if c == '#':
					comment_flag = 1
			else:
				comment_flag = 0


	print(content_tmp)
	content = content_tmp

	total = len(content)

	for step in range(1, 5):
		counter = defaultdict(int)
		for cc in range(len(content) - step + 1):
			counter[content[cc:cc+step]] += 1

		p = [x / total for x in counter.values()]

		entropy = -sum(x * log2(x) for x in p) / step
		print('step', step, ' ', entropy)

	print()


if __name__ == '__main__':
	#proc('f1.txt')
	#proc('f2.txt')
	#proc('eng.txt')
	for arg in sys.argv[1:]:
		proc(arg)