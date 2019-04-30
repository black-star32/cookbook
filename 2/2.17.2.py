# 你想将HTML或者XML实体如 &entity; 或 &#code; 替换为对应的文本。 再者，你需要转换文本中特定的字符(比如<, >, 或 &)
s = 'Elements are written as "<tag>text</tag>".'
import html
print(s)
print(html.escape(s))
# Disable escaping of quotes
print(html.escape(s, quote=False))
s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))

# 为了替换文本中的编码实体，你需要使用另外一种方法。 如果你正在处理HTML或者XML文本，试着先使用一个合适的HTML或者XML解析器。
# 通常情况下，这些工具会自动替换这些编码值，你无需担心。

# 如果你接收到了一些含有编码值的原始文本，需要手动去做替换， 通常你只需要使用HTML或者XML解析器的一些相关工具函数/方法即可。
s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
print(p.unescape(s))

t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))


