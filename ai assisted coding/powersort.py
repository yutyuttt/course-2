def powersort(array, key=None, reverse=False):
    """Sort a list in place using PowerSort's natural runs and node powers."""
    size = len(array)
    if size < 2:
        return array

    if key is None:
        key = lambda value: value

    keys = [key(value) for value in array]

    def less(first, second):
        return second < first if reverse else first < second

    runs = []
    start = 0
    while start < size:
        end = start + 1
        if end < size and less(keys[end], keys[start]):
            end += 1
            while end < size and less(keys[end], keys[end - 1]):
                end += 1
            array[start:end] = reversed(array[start:end])
            keys[start:end] = reversed(keys[start:end])
        else:
            while end < size and not less(keys[end], keys[end - 1]):
                end += 1
        runs.append((start, end))
        start = end

    def node_power(first, second):
        first_midpoint_twice = first[0] + first[1]
        second_midpoint_twice = second[0] + second[1]
        denominator = 2 * size
        power = 0
        while (first_midpoint_twice << power) // denominator == (
            second_midpoint_twice << power
        ) // denominator:
            power += 1
        return power

    def merge(first, second):
        start = first[0]
        middle = first[1]
        end = second[1]
        left_values = array[start:middle]
        left_keys = keys[start:middle]
        right_values = array[middle:end]
        right_keys = keys[middle:end]

        merged_values = []
        merged_keys = []
        left_index = 0
        right_index = 0
        while left_index < len(left_values) and right_index < len(right_values):
            if less(right_keys[right_index], left_keys[left_index]):
                merged_values.append(right_values[right_index])
                merged_keys.append(right_keys[right_index])
                right_index += 1
            else:
                merged_values.append(left_values[left_index])
                merged_keys.append(left_keys[left_index])
                left_index += 1

        merged_values.extend(left_values[left_index:])
        merged_values.extend(right_values[right_index:])
        merged_keys.extend(left_keys[left_index:])
        merged_keys.extend(right_keys[right_index:])
        array[start:end] = merged_values
        keys[start:end] = merged_keys
        return start, end

    pending_runs = [runs[0]]
    pending_powers = []
    for previous_run, current_run in zip(runs, runs[1:]):
        power = node_power(previous_run, current_run)
        while pending_powers and pending_powers[-1] >= power:
            right = pending_runs.pop()
            left = pending_runs.pop()
            pending_runs.append(merge(left, right))
            pending_powers.pop()
        pending_powers.append(power)
        pending_runs.append(current_run)

    while pending_powers:
        right = pending_runs.pop()
        left = pending_runs.pop()
        pending_runs.append(merge(left, right))
        pending_powers.pop()

    return array


power_sort = powersort
