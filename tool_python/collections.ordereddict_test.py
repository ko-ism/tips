import collections

od = collections.OrderedDict({'a':1, 'b':2, 'c':3})
d = {'a':1, 'b':2, 'c':3}

# return True
print(od == d)

od = collections.OrderedDict({'b':2, 'c':3, 'a':1})
d = {'a':1, 'b':2, 'c':3}

# return True
print(od == d)

od1 = collections.OrderedDict({'a':1, 'b':2, 'c':3})
od2 = collections.OrderedDict({'b':2, 'c':3, 'a':1})

# return False
print(od1 == od2)


## ソートすると見やすい
d = {'banana':1, 'apple':2, 'orange':3}
od = collections.OrderedDict(
    sorted(d.items() ,key=lambda t: t[0]) # keyでソート、1ならvalueの値でソート
)

# return OrderedDict([('apple', 2), ('banana', 1), ('orange', 3)])
print(od)
od['xxx'] = 100

# 追加すると必ず最後に入るので注意
# return OrderedDict([('apple', 2), ('banana', 1), ('orange', 3), ('xxx', 100)])
print(od)