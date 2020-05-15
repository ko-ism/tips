import re

## Greedy
s = '<html><head><title>Title</title></head></html>'

print(re.match('<.*>', s))
print(re.match('<.*?>', s))
