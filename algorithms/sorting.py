"""Merge Sort (O(n log n), stable) aur Quick Sort (avg O(n log n))."""
import random


def merge_sort(arr):
    if len(arr) <= 1:
        return list(arr)
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out


def quick_sort(arr):
    if len(arr) <= 1:
        return list(arr)
    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    more = [x for x in arr if x > pivot]
    return quick_sort(less) + equal + quick_sort(more)


def demo():
    data = random.sample(range(1, 50), 10)
    print("Input     :", data)
    print("MergeSort :", merge_sort(data))
    print("QuickSort :", quick_sort(data))
