import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0


class item:
    def __init__(self, name):
        self.name = name
    # 对应repr(object)这个函数,返回一个可以用来表示对象的可打印字符串
    def __repr__(self):
        return "Item({!r})".format(self.name)
