# Implement the Selection Sort algorithm using iteration

def selection_sort_iterative(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [64, 25, 12, 22, 11]
selection_sort_iterative(arr)
print("Iterative Selection Sort:", arr)
