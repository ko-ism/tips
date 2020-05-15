import collections

Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(19, y=20)
print(p.x)

# 値が代入できないクラスが生成されていることを確認
# 以下はError
# p.x = 100

p1 = Point._make([100,200])
print(p1.x)
print(p1._asdict())

p1._replace(x=50)
print(p1) ## replaceされていない
# 使うときは、以下。コピーして使う。
p2 = p1._replace(x=50)
print(p2)


class SumPoint(collections.namedtuple('Point', ['x', 'y'])):
    @property
    def total(self):
        return self.x + self.y

p3 = SumPoint(2,3)
print(p3.x, p3.y, p3.total)




import csv

# with open('names.csv', 'w') as csvfile:
#     fieldnames = ['first', 'last', 'address']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'first': 'Mike', 'last': 'Jackson', 'address': 'A'})
#     writer.writerow({'first': 'Jun', 'last': 'Sakai', 'address': 'B'})
#     writer.writerow({'first': 'Nancy', 'last': 'Mask', 'address': 'C'})

with open('names.csv', 'r') as f:
    csv_reader = csv.reader(f)
    Names = collections.namedtuple('_Names', next(csv_reader))
    # print(next(csv_reader))
    for row in csv_reader:
        names = Names._make(row)
        print(names.first, names.last, names.address)
