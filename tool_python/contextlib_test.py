import contextlib

def tag(f):
    def _wrapper():
        print('<h2>')
        r = f()
        print('</h2>')
        return r
    return _wrapper

@tag
def f():
    print('test')

f()
