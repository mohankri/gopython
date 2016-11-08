from collections import deque

def search(fh, pattern, history=5):
	prev_line = deque(maxlen=history)
	for line in fh:
		if pattern in line:
			yield line, prev_line
		prev_line.append(line)

def search_file():
	with open('readme.txt') as f:
		for line, prevlines in search(f, 'readme', 5):
			for pline in prevlines:
				print(pline, end='')
			print(line, end='')
			print('-'*20)


if __name__ == '__main__':
	search_file()
