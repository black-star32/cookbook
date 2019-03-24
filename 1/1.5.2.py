import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    # 对应repr(object)这个函数,返回一个可以用来表示对象的可打印字符串
    def __repr__(self):
        return "Item({!r})".format(self.name)


if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('qrok'), 1)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())