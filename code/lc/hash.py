d = dict()

d['a'] = 1
d['b'] = 2
d['c'] = 3
print(list(d.keys()))  # ['a', 'b', 'c']
print(type(d.values()))
d['y'] = 4
print(list(d.keys()))  # ['a', 'b', 'c', 'y']

d['d'] = 5
print(list(d.keys()))  # ['a', 'b', 'c', 'y', 'd']