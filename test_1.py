from collections import deque
while True:
    try:
        # 2 abc 123456789
        str1 = input()
        if not str1:
            break
        _deque = deque(str1.split())
        num = int(_deque.popleft())
        res = []
        while len(_deque):
            temp = _deque.popleft()
            if len(temp) < 8 :
                temp = temp + (8-len(temp))*'0'
                res.append(temp)
            elif len(temp) == 8:
                res.append(temp)
            else:
                res.append(temp[:8])
                _deque.appendleft(temp[8:])
        res = sorted(res)
        for ele in res:
            print(ele, end=' ')
    except:
        break