from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
d['a'].append(1)
print(d)

d1 = defaultdict(set)
d1['a'].add(1)
d1['a'].add(2)
d1['b'].add(4)
d1['a'].add(1)
print(d1)

pairs = [('a', 1), ('a', 2), ('b', 4), ('a', 1)]
d2 = defaultdict(list)
for key, value in pairs:
    d2[key].append(value)
print(d2)
