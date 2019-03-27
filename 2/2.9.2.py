# Unicode文本标准化,确保所有字符串在底层有相同的表示。
# 在Unicode中，某些字符能够用多个合法的编码表示。
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
print(s1 == s2)
print(len(s1))
print(len(s2))

import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
print(ascii(t1))
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3 == t4)
print(ascii(t3))

# normalize() 第一个参数指定字符串标准化的方式。
# NFC表示字符应该是整体组成(比如可能的话就使用单一编码)，
# 而NFD表示字符应该分解为多个组合字符表示。


# Python同样支持扩展的标准化形式NFKC和NFKD，
# 它们在处理某些字符的时候增加了额外的兼容特性。
# 比如：
s = '\ufb01' # A single character
print(s)
print(unicodedata.normalize('NFD', s))
# Notice how the combined letters are broken apart here
print(unicodedata.normalize('NFKD', s))
print(unicodedata.normalize('NFKC', s))

# 标准化对于任何需要以一致的方式处理Unicode文本的程序都是非常重要的。
# 当处理来自用户输入的字符串而你很难去控制编码的时候尤其如此。

# 在清理和过滤文本的时候字符的标准化也是很重要的。
# 比如，假设你想清除掉一些文本上面的变音符的时候(可能是为了搜索和匹配)：
t1 = unicodedata.normalize('NFD', s1)
res = ''.join(c for c in t1 if not unicodedata.combining(c))
print(res)

# 最后一个例子展示了 unicodedata 模块的另一个重要方面，也就是测试字符类的工具函数。
# combining() 函数可以测试一个字符是否为和音字符。
# 在这个模块中还有其他函数用于查找字符类别，测试是否为数字字符等等。