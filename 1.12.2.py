from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

words_counts = Counter(words)
# 出现频率最高的3个单词
top_three = words_counts.most_common(3)
print(top_three)

# 作为输入， Counter 对象可以接受任意的由可哈希（hashable）元素构成的序列对象。
# 在底层实现上，一个 Counter 对象就是一个字典，将元素映射到它出现的次数上。
print(words_counts['not'])
print(words_counts['eyes'])

# 手动增加计数，可以简单的用加法
morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
    words_counts[word] += 1
print(words_counts['eyes'])

# 或者你可以使用 update() 方法
words_counts.update(morewords)

# Counter 实例一个鲜为人知的特性是它们可以很容易的跟数学运算操作相结合。
a = Counter(words)
b = Counter(morewords)
print(a)
print(b)
# Combine counts
c = a + b
print(c)
# Subtract counts
d = a - b
print(d)