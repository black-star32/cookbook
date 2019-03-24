line = 'asdf fjdk; afed, fjek,asdf, foo'

import re
result = re.split(r'[;,\s]\s*', line)
print(result)

# 函数 re.split() 是非常实用的，因为它允许你为分隔符指定多个正则模式。
# 比如，在上面的例子中，分隔符可以是逗号，分号或者是空格，
# 并且后面紧跟着任意个的空格。 只要这个模式被找到，
# 那么匹配的分隔符两边的实体都会被当成是结果中的元素返回。
# 返回结果为一个字段列表，这个跟 str.split() 返回值类型是一样的。

# 当你使用 re.split() 函数时候，需要特别注意的是正则表达式中是否包含
# 一个括号捕获分组。 如果使用了捕获分组，那么被匹配的文本也将出现在结
# 果列表中。比如，观察一下这段代码运行后的结果：
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

# 获取分割字符在某些情况下也是有用的。 比如，你可能想保留分割字符串，
# 用来在后面重新构造一个新的输出字符串：
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)
# Reform the line using the same delimiters\
res = ''.join(v+d for v, d in zip(values, delimiters))
print(res)

# 如果你不想保留分割字符串到结果列表中去，但仍然需要使用到
# 括号来分组正则表达式的话， 确保你的分组是非捕获分组，形如 (?:...) 。
res = re.split(r'(?:,|;|\s)\s*', line)
print(res)
