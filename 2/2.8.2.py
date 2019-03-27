# 跨越多行去匹配
# 点(.)不能匹配换行符
import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a 
multiline comment */
'''
res1 = comment.findall(text1)
print(res1)
res2 = comment.findall(text2)
print(res2)

# 修改模式字符串，增加对换行的支持
# 在这个模式中， (?:.|\n) 指定了一个非捕获组
# (也就是它定义了一个仅仅用来做匹配，而不能通过单独捕获或者编号的组)。
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
res3 = comment.findall(text2)
print(res3)

# re.compile() 函数接受一个标志参数叫 re.DOTALL ，在这里非常有用。
# 它可以让正则表达式中的点(.)匹配包括换行符在内的任意字符。比如：
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
res4 = comment.findall(text2)
print(res4)