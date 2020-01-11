"""
Mapping Keys to Multiples Values in a Dict:

to easily construct such a dict, you can use defaultdict
from the collections. Problem: defaultdict creates entries for keys
accessed later.
"""

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)
print('This is a defaultdict: {0}'.format(d))

d['not_created_key']
print('The defautdict has added the new key: {0}'.format(d))

# this can be solved with normal dict and the use of the setdefault()

d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(3)

print('The normal dict with multiple values in a dict: {0}'.format(d))

# doing it yourself, would be like:
pairs = [('a', 1), ('a', 2), ('b', 3)]
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

print('This is a construction of multivalue dict: {0}'.format(d))
