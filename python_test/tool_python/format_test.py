# print('{name} {family}'.format(name='shinya', family='koizumi'))

# name = 'shinya'
# family = 'koizumi'
# print(f'{name} {family}')

# t = (1, 2, 3)
# print('{0[0]} {0[2]}'.format(t))
# # 一番これが分かりやすい
# print('{t[0]} {t[2]}'.format(t=t))
# print('{} {}'.format(t[0], t[2]))
# print('{0} {2}'.format(*t))

# # 辞書をキーワード引数で渡すこともできる。よくやる。
# d = {'name' : 'shinya', 'family': 'koizumi'}
# print('{name} {family}'.format(**d))

# print('{:<30}'.format('left'))
# print('{:>30}'.format('right'))
# print('{:^30}'.format('center'))
# print('{0:^30}'.format('center'))
# print('{0:*^30}'.format('center'))
# print('{name:*^30}'.format(name = 'center'))
# # 一番わかりやすいのは以下
# print('{name:{fill}{align}{width}}'.format(name = 'test', fill = '*', align = '^', width = 30))

# ３桁ずつカンマを入れてくれる機能もある
# print('{:,}'.format(123456789))

# print('{:+f} {:+f}'.format(3.14, -3.14))
# print('{:f} {:f}'.format(3.14, -3.14))
# print('{:-f} {:-f}'.format(3.14, -3.14))
# print('{}'.format(19/22))
# print('{:.2%}'.format(19/22))

print('{0:d} {1:d} {2:d}'.format(100,200,300))
print('{:d} {:d} {:d}'.format(100,200,300))
print(int(100), hex(100), oct(100), bin(100))
print('{0:d} {0:#x} {0:#o} {0:#b}'.format(100))
print('{0:d} {0:x} {0:o} {0:b}'.format(100))

for i in range(20):
    for base in 'bdX':
        print('{:5{base}}'.format(i, base=base), end= ' ')
    print()
    