import re
"""
match()     文字列の先頭で正規表現とマッチするか判定
search()    文字列を操作して、正規表現がどこにマッチするか調べる
findall()   正規表現にマッチする部分文字列をすべて洗い出しリストとして返す
finditer()  重複しないマッチオブジェクトのイテレータを返す
"""

# m = re.match('a.c', 'abc')
# print(m.group())

# m = re.search('a.c', 'test abc test')
# print(m)
# print(m.group())
# print(m.span())

# m = re.findall('a.c', 'test abc test abc')
# print(m)

# m = re.finditer('a.c', 'test abc test abc')
# print([w.group() for w in m])

# m = re.match('[a-zA-Z0-9_]', 'a')
# m = re.match('\w', 'a')
# print(m)

# m = re.match('[^a-zA-Z0-9_]', '@')
# m = re.match('\W', '@')
# print(m)

# m = re.match('[0-9]', '1')
# m = re.match('\d', '1')
# print(m)

# m = re.match('[^0-9]', 'x')
# m = re.match('\D', 'x')
# print(m)

# m = re.match('\s', ' ')
# print(m)

# m = re.search('^abc', 'abc test abc')
m = re.search('abc$', 'abc test abc')
print(m)