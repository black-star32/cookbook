# NumPy 库有一个矩阵对象可以用来解决这个问题。

# 矩阵类似于3.9小节中数组对象，但是遵循线性代数的计算规则。下面的一个例子展示了矩阵的一些基本特性：
import numpy as np
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
print(m)

# Return transpose
print(m.T)

# Return inverse
print(m.I)

# Create a vector and multiply
v = np.matrix([[2],[3],[4]])
print(v)
print(m * v)

# 可以在 numpy.linalg 子包中找到更多的操作函数，比如：
import numpy.linalg
# Determinant
print(numpy.linalg.det(m))
# Eigenvalues
print(numpy.linalg.eigvals(m))

# Solve for x in mx = v
x = numpy.linalg.solve(m, v)
print(x)
print(m*x)
print(v)
