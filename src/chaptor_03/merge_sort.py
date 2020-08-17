#归并排序
l=[49, 38, 65, 97, 76, 13, 27]


def merge_sort(data:list):
    # 拆分，分别排序
    if len(data) <= 1:
        return data
    mid = int(len(data)/2)
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    # 合并排序
    return merge(left, right)
# 合并排序
def merge(left:list, right:list):
    r, l = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += list(left[l:])
    result += list(right[r:])
    return result


print(merge_sort(l))




