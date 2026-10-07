def seq_search(key, array):
    i = 0
    found = False
    while (not found) and (i < len(array)):
        if array[i] == key:
            found = True
        i += 1
    return found

def time_search(algo, n, /, sort_data=False):
    import random, time

    data = random.choices(range(n), k=n)
    if sort_data: data.sort()
    key = n # never found, ensures worst case

    start = time.process_time()
    algo(key, data)
    end = time.process_time()
    return end - start

print(time_search(seq_search, 10**6))