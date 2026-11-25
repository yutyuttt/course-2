def insertion_sort(data: list) -> list:
    unsorted_data = data
    sorted_data = []

    # initially append first value from unsorted data to sorted data list to have a value to compare with
    sorted_data.append(unsorted_data.pop(0))

    for _ in range(len(unsorted_data)):
        data = unsorted_data.pop(0)
        sorted_data_length = len(sorted_data)
        
        for j in range(sorted_data_length):
            # check if value is smaller than value at index j.
            # if it is, insert value at correct index in sorted_data
            if data < sorted_data[j]:
                sorted_data.insert(j, data)
                break
            # if value is not smaller than every value in sorted_data, it must be largest value,
            # so append value to sorted_data
            elif j == sorted_data_length - 1:
                sorted_data.append(data)

    return sorted_data