# 字节字符串上的字符串操作

# 字节字符串同样也支持大部分和文本字符串一样的内置操作。比如：
data = b'Hello World'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

# 这些操作同样也适用于字节数组。比如：
data = bytearray(b'Hello World')
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

# 你可以使用正则表达式匹配字节字符串，但是正则表达式本身必须也是字节串。
# 比如：
data = b'FOO:BAR,SPAM'
import re
# re.split('[:,]',data)
print(re.split(b'[:,]', data))  # Notice: pattern as bytes