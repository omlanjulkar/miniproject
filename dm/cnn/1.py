# Implement the Selection Sort algorithm using recursion

def selection_sort_recursive(arr, start=0):
    if start >= len(arr) - 1:
        return
    min_index = start
    for i in range(start + 1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    arr[start], arr[min_index] = arr[min_index], arr[start]
    selection_sort_recursive(arr, start + 1)

arr = [64, 25, 12, 22, 11]
selection_sort_recursive(arr)
print("Recursive Selection Sort:", arr)
