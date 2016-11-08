from collections import defaultdict, OrderedDict
import json
'''
	d = {
		'a': [1, 2, 3],
		'b': [4, 5]
	}
'''
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

for args in d:
	print(args, d[args])

e = defaultdict(set)
e['a'].add(1);
e['a'].add(1);
e['b'].add(1);
e['a'].add(3);

for args in d:
	print(args, e[args])

# maintain doubly linked list
f = OrderedDict()
f['foo'] = 1
f['bar'] = 2
f['spam'] = 3
f['grok'] = 4

for args in f:
	print(args, f[args])

print(json.dumps(f))

price = {
	'ACME': 45.23,
	'AAPL': 612.78,
	'IBM': 205.55,
	'HPQ': 37.20,
	'FB':10.75
}

min_price = min(zip(price.values(), price.keys()))
print(min_price)

max_price = max(zip(price.values(), price.keys()))
print(max_price)

price_sorted=sorted(zip(price.values(), price.keys()))
print(price_sorted)

print(min(price, key=lambda k:price[k]))
print(min(price))

# 
# common keys in dict
#

a = {
	'x': 1,
	'y': 2,
	'z': 3
}

b = {
	'w': 1,
	'x': 11,
	'y': 2
}

print(a.keys() & b.keys())  ## common keys
print(a.keys() - b.keys())  ## keys not in b
print(a.items() & b.items()) ## common kv pair

#filter out dictionary content to new dict

c = {key:a[key] for key in a.keys() - {'z', 'w', 'x'}}
print(c)
