"""Binary Search - O(log n). Sorted array chahiye."""


def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def demo():
    data = [1, 3, 5, 7, 9, 11, 13]
    print("Array:", data)
    print("Search 7  ->", binary_search(data, 7))
    print("Search 4  ->", binary_search(data, 4))
