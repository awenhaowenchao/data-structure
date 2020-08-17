#选择排序
l=[49, 38, 65, 97, 76, 13, 27]


def choose_sort(data:list):
    dataen = len(data)
    for i in range(0, dataen-1):
        min = data[i]
        idx = i
        for j in range(i+1, dataen):
            # print("j=%s" % l[j])
            if data[j] < min:
                min = data[j]
                idx = j
        data[idx] = data[i]
        data[i] = min

    return data



print(choose_sort(l))