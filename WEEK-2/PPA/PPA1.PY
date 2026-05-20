def binarysearch(L, v):  #v = target element
    low = 0
    high = len(L) - 1
    i = 0
    while low <= high: 
        i += 1
        mid = (low + high) // 2
        if L[mid ] < v:
            low = mid  + 1
        elif L[mid ] > v:
            high = mid  - 1
        else:
            return (mid, i)
    return False

print(binarysearch([23, 4, 5, 6, 78, 90, 1, 2, 3], 6))

