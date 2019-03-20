from collections import OrderedDict
import json

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['qrok'] = 4

for key in d:
    print(key, d[key])

d2 = json.dumps(d)
print(d2)
