length = int(input())
input_lists = []
max_length = 0
while True:
        try:
            str1 = input()
            if not str1:
                break
            temp_list = str1.split(',')
            max_length = max(len(temp_list), max_length)
            input_lists.append([int(tem) for tem in temp_list])
        except:
            break
# input_lists
# print(input_lists)
# print(max_length)
result = []
index = 0
while max_length > 0:
    # print(max_length)
    # print(result)
    for i in range(len(input_lists)):
        if len(input_lists[i]) >= length:
            result.extend(input_lists[i][index:index+length])
            # input_lists[i] = input_lists[i][length:]
        elif len(input_lists[i]) == 0:
            continue
        else:
            result.extend(input_lists[i][index:])
            # input_lists[i] = []
    max_length -= length
    index += length
    # print(max_length)
    # print(input_lists)
print(','.join([str(res) for res in result]))


