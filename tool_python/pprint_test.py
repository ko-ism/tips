import json
import pprint

# l = ['apple', 'orange', 'banana']
# l.insert(0, l[:])
# # print(l)
# pp = pprint.PrettyPrinter(indent=4, width=40, compact=True, depth=3)
# pp.pprint(l)


# l = ['apple', 'orange', 'banana']
# print(json.dumps(l, indent=4))

from urllib.request import urlopen
with urlopen('https://pypi.org/pypi/sampleproject/json') as resp:
    project_info = json.load(resp)['info']

print(project_info)

pprint.pprint(project_info, depth=3)