"""
Implementing a Priority Queue
"""
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index = self._index + 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()

q.push(Item('item_01'), 1)
q.push(Item('item_02'), 5)
q.push(Item('item_03'), 4)
q.push(Item('item_04'), 1)

print(q._queue)

q.pop()  # pop 1
print('Item has been popped, queue is: \n {0}'.format(q._queue))
q.pop()  # pop 2
print('Item has been popped, queue is: \n {0}'.format(q._queue))
q.pop()  # pop 3
print('Item has been popped, queue is: \n {0}'.format(q._queue))
