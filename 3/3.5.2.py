# 你有一个字节字符串并想将它解压成一个整数。或者，你需要将一个大整数转换为一个字节字符串。

# 假设你的程序需要处理一个拥有128位长的16个元素的字节字符串。比如：
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
# 为了将bytes解析为整数，使用 int.from_bytes() 方法，并像下面这样指定字节顺序：
print(len(data))
print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))
# 为了将一个大整数转换为一个字节字符串，使用 int.to_bytes() 方法，并像下面这样指定字节数和字节顺序：
x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))
