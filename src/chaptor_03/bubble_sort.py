#冒泡排序
l=[49, 38, 65, 97, 76, 13, 27]


def bubble_sort(data:list):
    dataen = len(data)
    for i in range(0, dataen-1):
        # print("i=%s" % l[i])
        for j in range(i+1, dataen):
            # print("j=%s" % l[j])
            if data[i] > data[j]:
                tmp = data[i]
                data[i] = data[j]
                data[j] = tmp
                print(data)

bubble_sort(l)
print(l)