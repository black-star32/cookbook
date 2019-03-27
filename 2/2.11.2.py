# 删除字符串中不需要的字符
# Whitespace stripping
s = ' hello world \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# Character stripping
t = '-----hello====='
print(t.lstrip('-'))
print(t.rstrip('-='))

#  strip() 方法在读取和清理数据以备后续处理的时候是经常会被用到的。
#  比如，你可以用它们来去掉空格，引号和完成其他任务。
#　是需要注意的是去除操作不会对字符串的中间的文本产生任何影响。
s = ' hello     world \n'
s = s.strip()
print(s)
# 如果你想处理中间的空格，那么你需要求助其他技术。
# 比如使用 replace() 方法或者是用正则表达式替换。示例如下：
print(s.replace(' ', ''))
import re
print(re.sub('\s+', ' ', s))
# 通常情况下你想将字符串 strip 操作和其他迭代操作相结合，比如从文件中读取多行数据。
# 如果是这样的话，那么生成器表达式就可以大显身手了。比如：
with open('2.11.2.txt') as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)

# 在这里，表达式 lines = (line.strip() for line in f) 执行数据转换操作。
# 这种方式非常高效，因为它不需要预先读取所有数据放到一个临时的列表中去。
# 它仅仅只是创建一个生成器，并且每次返回行之前会先执行 strip 操作。