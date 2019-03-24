import heapq

# 堆是一个二叉树，其中每个父节点的值都小于或等于其所有子节点的值。整个堆的最小元素总是位于二叉树的根节点。python的heapq模块提供了对堆的支持。
# 堆数据结构最重要的特征是heap[0]永远是最小的元素

# heap为定义堆，item增加的元素
h = []
heapq.heappush(h, 2)
print(h)

# 将列表转换为堆
list = [1, 2, 3, 5, 1, 5, 8, 9, 6]
heapq.heapify(list)
print(list)

# 删除最小值，因为堆的特征是heap[0]永远是最小的元素，所以一般都是删除第一个元素。
print(list)
heapq.heappop(list)
print(list)

# 删除最小元素值，添加新的元素值
print(list)
heapq.heapreplace(list, 99)
print(list)

# 首先判断添加元素值与堆的第一个元素值对比，如果大，则删除第一个元素，然后添加新的元素值，否则不更改堆
print(list)
heapq.heappushpop(list, 6)
print(list)
heapq.heappushpop(list, 1)
print(list)

# 将多个堆合并
print(list)
h = [1000]
heapq.heapify(h)

for i in heapq.merge(h, list):
    print(i, end=" ")

# 查询堆中的最大元素，n表示查询元素个数
print(list)
print(heapq.nlargest(3, list))

# 查询堆中的最小元素，n表示查询元素的个数
print(list)
print(heapq.nsmallest(3, list))