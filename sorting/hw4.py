def selection_sort(array, n):
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


def read_words_from_url(url, stream=True):
    import requests

    response = requests.get(url, stream=True)
    words = [line.decode("utf-8".strip()) for line in response.iter_lines()]

    return words

import random

words = read_words_from_url("https://github.com/dwyl/english-words/raw/refs/heads/master/words.txt")
random.shuffle(words)
selection_sort(words, 1000)
print(words)

# running time of the sort increases quadratically with increasing n