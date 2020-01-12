def dedupe(items, key=None):
    """
    Eliminates duplicate values in a sequence
    if key is present in every dict in the
    sequence.
    """
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

def dedupe_mix_keys(items, key=None):
    seen = set()
    for item in items:
        if key is None:
            val = item
        else:
            try:
                val = key(item)
            except:
                pass
            if val not in seen:
                yield item
                seen.add(val)

a = [{'a': 1, 'b': 2, 'c': 3}, {'a': 2, 'x': 4},
     {'z': 1, 'f': 4}, {'z': 1, 'a': 4}]
# print(list(dedupe(a, key=lambda d: (d['a']))))  # raises an error key
print(list(dedupe_mix_keys(a, key=lambda d: (d['a']))))  # raises an error key

