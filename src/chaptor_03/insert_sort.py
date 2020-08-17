#插入排序
l=[49, 38, 65, 97, 76, 13, 27]


def insert_sort(data:list):
    dataen = len(data)
    for i in range(1, dataen):
        # print("i=%s" % l[i])
        for j in range(0, i):
            # print("j=%s" % l[j])
            if l[j] > l[i]:
                tmp = l[j]
                l[j] = l[i]
                l[i] = tmp
                print(data)
    return data



print(insert_sort(l))