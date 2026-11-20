def seq_search(key, array):
    i = 0
    found = False
    while (not found) and (i < len(array)):
        if array[i] == key:
            found = True
        i += 1
    return found

arr = [7, -22, 4, 56, 8]
print(seq_search(4, arr))
print(seq_search(57, arr))
