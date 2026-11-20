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
        print(array)


def bubble_sort(array):
    n = len(array)
    ordered = False
    while not ordered:
        ordered = True
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                (array[i], array[i + 1]) = (array[i + 1], array[i])
                ordered = False
            print(array)


data = [-4, 11, 7, -12, 6, 1]
selection_sort(data)
print(data)

print()

data = [-4, 11, 7, -12, 6, 1]
bubble_sort(data)
print(data)