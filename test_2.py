
# # it = re.finditer(r"\d+","12a32bc43jf3")
# # for match in it:
# #     print(match.group() )
#
# # "abc3(A)"
# pattern = r"(\d+)(\(|\)|\[|\]|\{|\})+([a-zA-Z]+)(\(|\)|\[|\]|\{|\})"
# str1 = "abc3(A)2{b}sadfs32[ds]"
# it = re.finditer(pattern, str1)
# res = []
# for match in it:
#     # print(match.group())
#     # print(match.group(1))
#     # print(match.group(3))
#     res.append((match.group(), int(match.group(1))*match.group(3)))
#     # str1.replace(match.group(), int(match.group(1))*match.group(3))
# print(res)
# for ele in res:
#     # print(ele[0])
#     # print(ele[1])
#     str1.replace(ele[0], ele[1])


import re
str1 = input()
pattern = r"(\d+)(\(|\)|\[|\]|\{|\})+([a-zA-Z]+)(\(|\)|\[|\]|\{|\})"

def rep(matched):
    res = int(matched.group(1)) * matched.group(3)
    return res

print(re.sub(pattern, rep, str1)[::-1])
