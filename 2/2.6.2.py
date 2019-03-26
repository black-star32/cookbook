# 以忽略大小写的方式搜索与替换文本字符串
# 为了在文本操作时忽略大小写，你需要在使用 re 模块的时候
# 给这些操作提供 re.IGNORECASE 标志参数。比如：
import re
text = 'UPPER PYTHON, lower python, Mixed Python'
res1 = re.findall('python', text, flags=re.IGNORECASE)
print(res1)
res2 = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(res2)

# 最后的那个例子揭示了一个小缺陷，替换字符串并不会自动跟被匹配字符串的大小写保持一致。
# 为了修复这个，你可能需要一个辅助函数，就像下面的这样：
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

res3 = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(res3)

# matchcase('snake') 返回了一个回调函数(参数必须是 match 对象)，前面一节提到过，
# sub() 函数除了接受替换字符串外，还能接受一个回调函数。

