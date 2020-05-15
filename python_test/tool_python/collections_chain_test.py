import collections

a = {'a': 'a', 'c': 'c', 'num': 0}
b = {'b': 'b', 'c': 'cc'}
c = {'b':'bbb', 'c': 'ccc'}

# classで作成
class DeepChainMap(collections.ChainMap):
    def __setitem__(self, key, value):
        for mapping in self.maps:
            if type(mapping[key]) is int and mapping[key] < value:
                mapping[key] = value
            return
        self.maps[0][key] = value

m = DeepChainMap(a, b, c)
# m['num'] = 5
# print(m['num'])

m['num'] = -1
print(m['num'])


## updateはどんどん上書かれる
# print(a)
# a.update(b)
# print(a)
# a.update(c)
# print(a)

# ## collections.ChainMapを使うと履歴が分かる
# m = collections.ChainMap(a, b, c)
# print(m)
# m.maps.reverse()
# print(m.maps)
# m.maps.insert(0, {'c': 'CCCC'})
# print(m.maps)
# print(m['c'])
# print(m.maps[0])
# del m.maps[0]
# print(m.maps)
# print(m['c'])
# m['b'] = 'BBBBB'
# print(m.maps)