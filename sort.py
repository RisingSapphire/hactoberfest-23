import random
import time

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Helper function to generate a random list of numbers
def generate_random_list(size):
    return [random.randint(1, 1000) for _ in range(size)]

if __name__ == "__main__":
    list_size = 1000
    random_list = generate_random_list(list_size)

    # Bubble Sort
    bubble_list = random_list.copy()
    bubble_start = time.time()
    bubble_sort(bubble_list)
    bubble_time = time.time() - bubble_start

    # Selection Sort
    selection_list = random_list.copy()
    selection_start = time.time()
    selection_sort(selection_list)
    selection_time = time.time() - selection_start

    # Insertion Sort
    insertion_list = random_list.copy()
    insertion_start = time.time()
    insertion_sort(insertion_list)
    insertion_time = time.time() - insertion_start

    # Merge Sort
    merge_list = random_list.copy()
    merge_start = time.time()
    merge_sort(merge_list)
    merge_time = time.time() - merge_start

    # Quick Sort
    quick_list = random_list.copy()
    quick_start = time.time()
    quick_sort(quick_list)
    quick_time = time.time() - quick_start

    print(f"List size: {list_size}")
    print(f"Bubble Sort Time: {bubble_time:.6f} seconds")
    print(f"Selection Sort Time: {selection_time:.6f} seconds")
    print(f"Insertion Sort Time: {insertion_time:.6f} seconds")
    print(f"Merge Sort Time: {merge_time:.6f} seconds")
    print(f"Quick Sort Time: {quick_time:.6f} seconds")
