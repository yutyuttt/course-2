# 1. The minimum value of i must be l, so i = l + ...
#    Next, we find the "progress" of k through vl to vh, e.g. k being 60% of the way from vl to vh
#    The formula for this is (k - vl)/(vh - vl)
#    Then, to get the index, multiply the "progress" by (h - l)
#    The final formula would be i = l + (k - vl)/(vh - vl) * (h - l)

# 2. 1. i = 0 + (200 - 0)/(100 - 0) * (1 - 0) = 2 * 1 = 2
# 2. 2. The algorithm would give an undefined index if k < vl or k > vh

# 3. The value of i should be h or l

# 4
def interpolation_search(key, array):
    low = 0
    high = len(array) - 1

    while low <= high and array[low] <= key <= array[high]:
        if low == high:
            i = low
        else:
            i = low + (key - array[low]) / (array[high] - array[low]) * (high - low)
        i = int(i)

        if array[i] == key: return i
        if array[i] < key:
            low = i + 1
        else: high = i - 1

    return False


arr = [-22, 4, 7, 8, 8, 56]
print(interpolation_search(4, arr))