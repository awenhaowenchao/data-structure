#希尔排序
l=[49, 38, 65, 97, 76, 13, 27]

def shell_sort(data:list):
    n = len(data)
    gap = int(n / 2)
    while gap > 0:
        for i in range(gap, n):
            temp = data[i]
            j = i - gap
            while j >= 0 and data[j] > temp:
                data[j + gap] = data[j]
                j = j - gap
            data[j + gap] = temp
        gap = int(gap / 2)
    return data

print(shell_sort(l))