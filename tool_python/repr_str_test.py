# reprメソッドは、オブジェクトを表示できる
import datetime
d = datetime.datetime.now()
print(d)
print(repr(d))

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return 'Point<object>'

    def __str__(self):
        return 'Point ({}, {})'.format(self.x, self.y)
    
p = Point(10,100)
print('{0!r}'.format(p))
print('{0}'.format(p))
print('{0!s}'.format(p))