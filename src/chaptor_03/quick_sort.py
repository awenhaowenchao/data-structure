#快速排序
l=[49, 38, 65, 97, 76, 13, 27]


def quick_sort(data:list):
    if len(data) > 1:
        midx = int(len(data) / 2)
        mid = data[midx]
        print("midx=%s" % midx)
        left = []
        right = []
        for i in range(0, len(data)):
            if i!=midx:
                if data[i]>mid:
                    right.append(data[i])
                else:
                    left.append(data[i])
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data


print(quick_sort(l))