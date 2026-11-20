# 1.1 Sequential search does 7 comparisons when searching for the key
# 1.2 Binary search does 2 comparisons

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
        print(array[mid], key)
    return False

arr = [-2, 9, 11, 12, 13, 14, 15, 22, 142]
bin_search(15, arr)