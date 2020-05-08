import collections
import queue

# Double-end queue
collections.deque

# queue
q = queue.Queue()
lq = queue.LifoQueue()

# List
l = []

# collections.deque()
d = collections.deque()

for i in range(3):
    q.put(i)
    lq.put(i)
    l.append(i)
    d.append(i)

# print(d)
# print(d[1])
# d.rotate()
# print(d)
# d.rotate()
# print(d)

# ## deque([0, 1, 2])
# print(d)
# d.extendleft('x')
# d.extend('y')
# ## deque(['x', 0, 1, 2, 'y'])
# print(d)
d.clear()
print(d)


for _ in range(3):
    ## FIFO
    print(f'FIFO queue = {q.get()}')
    ## LIFO
    print(f'FIFO queue = {lq.get()}')
    ## LIFO
    print(f'FIFO queue = {l.pop()}')
    ## FIFO
    # print(f'FIFO queue = {l.pop(0)}')
    ## LIFO
    print(f'FIFO queue = {d.pop()}')
    ## FIFO
    # print(f'FIFO queue = {d.popleft()}')
    print('')
