# Insertion sort 
# define a fuction
def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] :          #  Insertion sort logic
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    arr =[]
    n = int(input("Enter the number of elements: "))
    for i in range(0, n):               #  Taking input from user
        ele = int(input())
        arr.append(ele)
    print("Unsorted list: ", arr)

    print("Array before sorting: ", arr)            #  Printing unsorted list
    print(insertionSort(list))
