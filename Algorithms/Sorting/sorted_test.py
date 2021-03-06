import bubble
import insertion
import merge_sort
import quick
import selection


def unsorted():
    import random

    before = random.sample(range(1, 1000000), 10000)

    return before


if __name__ == '__main__':
    import time

    before = unsorted()
    print(before)

    # bubble
    start_b = time.time()
    sorted_bubble = bubble.bubble(before)
    print(sorted_bubble)
    end_b = time.time()
    print('bubble', end_b - start_b)

    # selection
    start_s = time.time()
    sorted_selection = selection.selection(before)
    print(sorted_selection)
    end_s = time.time()
    print('selection', end_s - start_s)

    # insertion
    start_i = time.time()
    sorted_insertion = insertion.insertion(before)
    print(sorted_insertion)
    end_i = time.time()
    print('insertion', end_i - start_i)

    # quick
    start_q = time.time()
    sorted_quick = quick.quick(before)
    print(sorted_quick)
    end_q = time.time()
    print('quick', end_q - start_q)

    # merge
    start_m = time.time()
    sorted_merge = merge_sort.devide(before)
    print(sorted_merge)
    end_m = time.time()
    print('merge', end_m - start_m)
