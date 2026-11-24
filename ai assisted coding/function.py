# function returning two largest value in a list
def two_largest(lst):
    if len(lst) < 2:
        return "List must contain at least two elements."

    first = second = None

    for value in lst:
        if first is None or value >= first:
            second = first
            first = value
        elif second is None or value > second:
            second = value

    return (first, second)


def equal_sum_partitions(lst):
    """Return all contiguous partitionings whose parts have equal sums."""
    size = len(lst)
    if size == 0:
        return []

    prefix_sums = [0]
    for value in lst:
        prefix_sums.append(prefix_sums[-1] + value)

    total = prefix_sums[-1]
    partitionings = []

    for part_count in range(1, size + 1):
        if total % part_count != 0:
            continue

        target = total // part_count
        parts = []

        def find_partitions(start, remaining):
            if remaining == 1:
                if prefix_sums[size] - prefix_sums[start] == target:
                    partitionings.append(parts + [lst[start:]])
                return

            last_end = size - remaining + 1
            for end in range(start + 1, last_end + 1):
                if prefix_sums[end] - prefix_sums[start] == target:
                    parts.append(lst[start:end])
                    find_partitions(end, remaining - 1)
                    parts.pop()

        find_partitions(0, part_count)

    return partitionings