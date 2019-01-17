def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    while len(left) > 0:
        result.append(left[0])
        left.pop(0)
    while len(right) > 0:
        result.append(right[0])
        right.pop(0)
    print(result)
    return result


def mergesort(m):
    if len(m) <= 1:
        return m
    else:
        middle = len(m) // 2
        left = m[:middle]
        right = m[middle:]
    left = mergesort(left)
    right = mergesort(right)
    result = merge(left, right)
    return result


print(mergesort([7, 3, 4, 9, 10, 20, 21]))
