import copy
import timeit
import random


# Insertion sort
def insertion_sort(array):
    arr = copy.copy(array)  # to keep the original
    for i in range(1, len(arr)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Merge sort
def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    sorted_array = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array


# Test data

test_data = {
    "small_random": [random.randint(1, 100) for _ in range(10)],
    "large_random": [random.randint(1, 1000) for _ in range(1000)],
    "sorted": list(range(1, 101)),
    "reversed": list(range(100, 0, -1)),
    "duplicates": [random.choice([1, 2, 3]) for _ in range(100)],
}


for name, data in test_data.items():
    print(f"Testing on {name} dataset:")
    print(
        f"Built-in sorted: {timeit.timeit(lambda: sorted(data), number=1000):.6f} seconds"
    )
    print(
        f"Built-in sort(): {timeit.timeit(lambda: copy.copy(data).sort(), number=1000):.6f} seconds"
    )
    print(
        f"Insertion sort: {timeit.timeit(lambda: insertion_sort(data), number=1000):.6f} seconds"
    )
    print(
        f"Merge sort: {timeit.timeit(lambda: merge_sort(data), number=1000):.6f} seconds"
    )
    print()
