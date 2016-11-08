#!/usr/bin/env python3
import sys

sys.path.insert(0, './module1')

import module1
print (module1.ageofqueen)

def iter_array():
	p = (4, 5)
	x, y = p
	print (x)

iter_array()

records = [ ('foo', 1, 2),
	   ('bar', 'hello'),
	   ('foo', 3, 4),
	 ]

def do_foo(x, y):
	print('foo', x, y)

def do_bar(s):
	print('bar', s)

for tag, *args in records:
	print (tag)
	if tag == 'foo':
		do_foo(*args)
	elif tag == 'bar':
		do_bar(*args)
