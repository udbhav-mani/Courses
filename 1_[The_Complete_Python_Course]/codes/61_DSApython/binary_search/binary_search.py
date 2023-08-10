def binary_search(list, key):
    length = len(list)
    
    mid = 0
    l = 0
    r = length - 1

    while l <= r:
        mid = (l + r) // 2
        if key > list[mid]:
            l = mid + 1
        elif key < list[mid]:
            r = mid - 1
        else:
            return mid

    return -1


list = list(range(1, 11))

print(binary_search(list, 6))
