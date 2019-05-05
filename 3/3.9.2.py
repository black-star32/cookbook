# 涉及到数组的重量级运算操作，可以使用 NumPy 库。
# NumPy 的一个主要特征是它会给Python提供一个数组对象，
# 相比标准的Python列表而已更适合用来做数学运算。
# 下面是一个简单的小例子，向你展示标准列表对象和 NumPy 数组对象之间的差别：

# Python lists
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print(x * 2)
# print(x + 10)
print(x + y)

# Numpy arrays
import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print(ax * 2)
print(ax + 10)
print(ax + ay)
print(ax * ay)

# 正如所见，两种方案中数组的基本数学运算结果并不相同。 特别的， NumPy 中的标量运算(比如 ax * 2 或 ax + 10 )会作用在每一个元素上。 另外，当两个操作数都是数组的时候执行元素对等位置计算，并最终生成一个新的数组。

# 对整个数组中所有元素同时执行数学运算可以使得作用在整个数组上的函数运算简单而又快速。 比如，如果你想计算多项式的值，可以这样做：
def f(x):
    return 3*x**2 - 2*x + 7

print(f(ax))

# NumPy 还为数组操作提供了大量的通用函数，这些函数可以作为 math 模块中类似函数的替代。比如：
print(np.sqrt(ax))
print(np.cos(ax))

# 使用这些通用函数要比循环数组并使用 math 模块中的函数执行计算要快的多。 因此，只要有可能的话尽量选择 NumPy 的数组方案。
# 底层实现中， NumPy 数组使用了C或者Fortran语言的机制分配内存。 也就是说，它们是一个非常大的连续的并由同类型数据组成的内存区域。 所以，你可以构造一个比普通Python列表大的多的数组。 比如，如果你想构造一个10,000*10,000的浮点数二维网格，很轻松：

grid = np.zeros(shape=(10000,10000), dtype=float)
print(grid)

# 所有的普通操作还是会同时作用在所有元素上：
grid += 10
print(grid)
print(np.sin(grid))

# 关于 NumPy 有一点需要特别的主意，那就是它扩展Python列表的索引功能 - 特别是对于多维数组。 为了说明清楚，先构造一个简单的二维数组并试着做些试验：
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
# Select row 1
print(a[1])
# Select column 1
print(a[:,1])
# Select a subregion and change it
print(a[1:3, 1:3])
a[1:3, 1:3] += 10
print(a)
# Broadcast a row vector across an operation on all rows
print(a + [100, 101, 102, 103])
print(a)
# Conditional assignment on an array
print(np.where(a < 10, a, 10))
