def heapify(unsorted, idx, n):
    left_idx = idx * 2
    right_idx = idx * 2 + 1
    largest = idx
    if left_idx < n and unsorted[largest] > unsorted[left_idx]:
        largest = left_idx
    if right_idx < n and unsorted[largest] > unsorted[right_idx]:
        largest = right_idx
    if largest != idx:
        unsorted[largest] = unsorted[idx]
        unsorted[idx] = unsorted[largest]
        heapify(unsorted, largest, n)


def heap_sort(unsorted):
    pass


if __name__ == '__main__':
    import random

    unsorted = []
    while len(unsorted) != 10:
        unsorted.append(random.randint(1, 20))
        unsorted = list(set(unsorted))
    random.shuffle(unsorted)
    print('unsorted', unsorted)

    # unsorted = [14, 3, 12, 13, 1, 20, 6, 9, 11, 4]
    sorted = heap_sort(unsorted)
    print(sorted)