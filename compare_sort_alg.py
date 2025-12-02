import copy
import timeit

#  Array to sort
# arr = [5, 6, 2, 8, 1, 9, 3, 4, 7]
arr = [15, 3, 27, 8, 42, 19, 33, 7, 21, 4, 50, 2, 11, 39, 6]


# Built-in sorted
sorted_arr_py = sorted(arr)
print(f"Sorted array by Python: {sorted_arr_py}")

# Measure runtime for built-in sorted
sorted_time = timeit.timeit(lambda: sorted(arr), number=1000)
print(f"Built-in sorted runtime: {sorted_time:.6f} seconds")

# Built-in sort()
copy_arr = copy.copy(arr)

# Measure runtime for built-in sort()
sort_method_time = timeit.timeit(lambda: copy_arr.sort(), number=1000)
print(f"Built-in Sort() runtime: {sort_method_time:.6f} seconds")


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


insert_arr = insertion_sort(arr)
print(f"Insertion sort: {insert_arr}")

# Measure runtime for insertion sort
insertion_sort_time = timeit.timeit(lambda: insertion_sort(arr), number=1000)
print(f"Insertion sort runtime: {insertion_sort_time:.6f} seconds")


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


merge_sorted_arr = merge_sort(arr)
print(f"Merge sort: {merge_sorted_arr}")

# Measure runtime for merge sort
merge_sort_time = timeit.timeit(lambda: merge_sort(arr), number=1000)
print(f"Merge sort runtime: {merge_sort_time:.6f} seconds")
