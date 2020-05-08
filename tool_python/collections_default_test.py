import collections

d = {}
l = ['a', 'a', 'a', 'b', 'b', 'c']

for word in l:
    if word not in d:
        d[word] = 0
    d[word] += 1
print(d)


d = {}
l = ['a', 'a', 'a', 'b', 'b', 'c']
for word in l:
    d.setdefault(word, 0)
    d[word] += 1
print(d)


d = collections.defaultdict(int)
l = ['a', 'a', 'a', 'b', 'b', 'c']
for word in l:
    d[word] += 1
print(d)


## ただのカウンターではなく、集合として使うことも容易
d = collections.defaultdict(set)
s = [('red', 1), ('red', 2), ('red', 3), 
    ('blue', 2), ('blue', 4), 
    ('green', 1), ('green', 3)]
for k, v in s:
    d[k].add(v)
print(d)