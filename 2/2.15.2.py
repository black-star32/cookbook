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

# # format 和 format_map() 的一个缺陷就是它们并不能很好的处理变量缺失的情况
# # print(s.format_map(name='Guido'))

# 一种避免这种错误的方法是另外定义一个含有 __missing__() 方法的字典对象，就像下面这样
class safesub(dict):
    """防止key找不到"""
    def __missing__(self, key):
        return '{' + key + '}'

# 现在你可以利用这个类包装输入后传递给 format_map() ：
name = 'Guido'
print(s.format_map(safesub(vars())))

# 如果你发现自己在代码中频繁的执行这些步骤，你可以将变量替换步骤用一个工具函数封装起来。就像下面这样：
import sys

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} messages.'))
print(sub('Your favorite color is {color}'))