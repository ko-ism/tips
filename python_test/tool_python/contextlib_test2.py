import contextlib

# def tag(name):
#     def _tag(f):
#         def _wrapper(content):
#             print(f'<{name}>')
#             r = f(content)
#             print(f'</{name}>')
#             return r
#         return _wrapper
#     return _tag

# @tag('h2')
# def f(content):
#     print(content)

# # f = tag('h2')(f)
# f('text')


@contextlib.contextmanager
def tag(name):
    print(f'<{name}>')
    yield
    print(f'</{name}>')

# @tag('h2')
# def f(content):
#     print(content)

# f('text')

with tag('h2'):
    print('text')