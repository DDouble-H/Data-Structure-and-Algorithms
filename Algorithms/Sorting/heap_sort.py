def heapify(unsorted, idx, n):
    left_idx = idx * 2 + 1
    right_idx = idx * 2 + 2
    largest = idx
    if left_idx < n and unsorted[largest] > unsorted[left_idx]:  # 왼쪽 자식 노드가 현재 노드보다 크면 인덱스 변경
        largest = left_idx
    if right_idx < n and unsorted[largest] > unsorted[right_idx]:  # 오른쪽 자식 노드가 현재 노드보다 크면 인덱스 변경
        largest = right_idx
    if largest != idx:  # 변경된 인덱스와 largest 값 변경
        unsorted[largest], unsorted[idx] = unsorted[idx], unsorted[largest]
        heapify(unsorted, largest, n)  # 변경된 부분 기준으로 재정렬


def heap_sort(unsorted):
    n = len(unsorted)
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        # unsorted[i] = unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted


if __name__ == '__main__':
    import random

    unsorted = []
    while len(unsorted) != 10:
        unsorted.append(random.randint(1, 20))
        unsorted = list(set(unsorted))
    random.shuffle(unsorted)
    print('unsorted', unsorted)

    sorted = heap_sort(unsorted)
    print('sorted', sorted)