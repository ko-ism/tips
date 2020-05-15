import re

# s = 'My name is ... Mike'
# print(s.split())
# p = re.compile(r'\W+')
# print(p.split(s))
# # result is
# # ['My', 'name', 'is', '...', 'Mike']
# # ['My', 'name', 'is', 'Mike']


p = re.compile('(blue|white|red)')
print(p.sub('colour', 'blue socks and red shoes', ))
print(p.sub('colour', 'blue socks and red shoes', count=1))
print(p.subn('colour', 'blue socks and red shoes', ))


def hexrpl(match):
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d')
print(p.sub(hexrpl, '12345 55 11 test test2'))
# print(re.sub(p, hexrpl, '12345 55 11 test test2'))