# Selecion sort 

#define a fuction
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:          #  Selection sort logic
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == "__main__":
    arr =[] # empty list
    n = int(input("Enter the number of elements: "))
    for i in range(0, n):           #  Taking input from user   
        ele = int(input())
        arr.append(ele)
    print("Unsorted list: ", arr)

    print("Array before sorting: ", arr)        #  Printing unsorted list
    print(selection_sort(list))