#!/usr/bin/env python3

#
# tuples of varying length
#
record = [ ('foo', 1, 2),
	   ('bar', 1),
	   ('foo', 3, 4),
	]

def handle_foo(args):
	print (args)
	x, y = args
	print (x, y)

def handle_bar(args):
	print (args)
	
items = [1, 10, 7, 4, 5, 9]

for fn, *args in record:
	if fn == 'foo':
		handle_foo(args)
	elif fn == 'bar':
		handle_bar(args)

def sum(items):
	head, *tails = items;
	return head + sum(tails) if tails else head



total = sum(items)

print (total)



