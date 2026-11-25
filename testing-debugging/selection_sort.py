def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        # get the smallest value in a dataset
        smallest = array[i]
        smallest_index = i
        for j in range(i + 1, n):
            if array[j] < smallest:
                smallest = array[j]
                smallest_index = j

        # swap if necessary
        if smallest_index != i:
            (array[i], array[smallest_index]) = (array[smallest_index], array[i])
        
arr = [7, 9, 2, 11]
selection_sort(arr)
print(arr)


def time_sort(algo, n):
    import time, random

    data = random.choices(range(n), k=n)

    start = time.process_time()
    algo(data)
    end = time.process_time()
    return end - start

print(time_sort(selection_sort, 2000))