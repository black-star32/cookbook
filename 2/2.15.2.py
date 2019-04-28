# 创建一个内嵌变量的字符串，变量被它的值所表示的字符串替换掉。
s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))

# # 如果要被替换的变量能在变量域中找到， 那么你可以结合使用 format_map() 和 vars()
# name = 'Guido'
# n = 37
# print(s.format_map(vars()))

# vars() 还有一个有意思的特性就是它也适用于对象实例。
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Guido', 37)
print(s.format_map(vars(a)))

# format 和 format_map() 的一个缺陷就是它们并不能很好的处理变量缺失的情况
print(s.format_map(name='Guido'))