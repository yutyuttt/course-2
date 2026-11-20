def bin_search(key, array):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == key: return mid
        if array[mid] < key:
            print(mid, key, array[mid])
            left = mid + 1
        else: right = mid - 1
    return False


arr = [-22, 4, 7, 8, 8, 56]
print(bin_search(4, arr))
print(bin_search(57, arr))