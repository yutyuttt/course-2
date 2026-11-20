def read_words_from_url(url):
    import requests

    response = requests.get(url, stream=True)
    words = [line.decode("utf-8").strip() for line in response.iter_lines()]

    return words


def seq_search(key, array):
    i = 0
    found = False
    while (not found) and (i < len(array)):
        if array[i] == key:
            found = True
        i += 1
    return found


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


# 1
words = read_words_from_url("https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words_alpha.txt")
last_words = words[-10:]
for word in last_words:
    print(word)


# 2
print(seq_search("protege", words))
print(bin_search("protege", words))


# 3
import time
start = time.time()
print("Starting sequential search")
seq_search("protege", words)
end = time.time()
print(f"Sequential search completed in {end - start}")

start = time.time()
print("Starting binary search")
bin_search("protege", words)
end = time.time()
print(f"Binary search completed in {end - start}")