import re

def rep(matched):
    res = int(matched.group(1)) * matched.group(3)
    return res

while True:
    try:
        str1 = input()
        if not str1:
            break
        pattern = r"(\d+)(\(|\)|\[|\]|\{|\})+([a-zA-Z]+)(\(|\)|\[|\]|\{|\})"
        print(re.sub(pattern, rep, str1)[::-1])
    except:
        break