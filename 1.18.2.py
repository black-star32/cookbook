# collections.namedtuple() 实际上是一个返回 Python 中标准元组类型子类的一个工厂方法。
# 你需要传递一个类型名和你需要的字段给它，然后它就会返回一个类，
# 你可以初始化这个类，为你定义的字段传递值等。

from collections import namedtuple

Subscriber = namedtuple('Subsciber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)

# 尽管 namedtuple 的实例看起来像一个普通的类实例，但是它跟元组类型是可交换的，
# 支持所有的普通元组操作，比如索引和解压。
print(len(sub))
addr, joined = sub
print(addr)
print(joined)


# 命名元组的一个主要用途是将你的代码从下标操作中解脱出来。
# 因此，如果你从数据库调用中返回了一个很大的元组列表，通过下标去操作其中的元素，
# 当你在表中添加了新的列的时候你的代码可能就会出错了。

# 使用普通元组的代码
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


# 下标操作通常会让代码表意不清晰，并且非常依赖记录的结构。
# 下面是使用命名元组的版本

Stock = namedtuple('Stock', ['name', 'share', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.share * s.price
    return total

s = Stock('ACME', 100, 123.45)
print(s)
# print(s.share=75)  一个命名元组是不可更改的

# 如果你真的需要改变属性的值，
# 那么可以使用命名元组实例的 _replace() 方法，
# 它会创建一个全新的命名元组并将对应的字段用新的值取代。
s = s._replace(share=75)
print(s)

# _replace() 方法还有一个很有用的特性就是当你的命名元组拥有可选或者缺失字段时候，
# 它是一个非常方便的填充数据的方法。 你可以先创建一个包含缺省值的原型元组，
# 然后使用 _replace() 方法创建新的值被更新过的实例。
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)
# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)
