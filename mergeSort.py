# 合并函数
def merge(left, right):
    merged = []
    i, j = 0, 0
    left_len, right_len = len(left), len(right)
    while i < left_len and j < right_len:
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# 拆分函数


def mergeSort(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2
    left = mergeSort(a[:mid])
    right = mergeSort(a[mid:])
    return merge(left, right)


a = [98, 23, 45, 14, 9, 67, 33, 108]
a1 = mergeSort(a)
print(a1)
