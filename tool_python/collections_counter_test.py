import collections

l = ['a', 'a', 'a', 'b', 'b', 'c']
d = collections.Counter()
for word in l:
    d[word] += 1
print(d)
print(d.most_common(1))
print(d.values())
print(sum(d.values()))

import re

with open('collections_counter_test.py', 'r', encoding='utf-8') as f:
    words = re.findall(r'\w+', f.read().lower())
    print(words)
    print(collections.Counter(words).most_common(20))