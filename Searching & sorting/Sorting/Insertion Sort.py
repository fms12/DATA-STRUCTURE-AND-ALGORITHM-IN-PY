# Insertion sort is a simple sorting algorithm with a complexity of n^2

def insertionSort(L):
    # storing the array in arr
    arr=L

    for i in range(1, len(arr)):
        #iterating the array
        key = arr[i] # let key be the current element
        j = i-1 

        # Moving the elements of array greater than key, to one position ahead of their current position
        while j >= 0 and key < arr[j]: 
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr # returning the sorted array.

# Sample Case
sample_array = [12, 11, 13, 5, 6]
print(insertionSort(sample_array))