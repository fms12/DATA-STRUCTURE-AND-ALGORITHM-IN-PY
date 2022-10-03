# Bubble sort
# define a fuction
def bubble_sort(list):      
    for i in range(len(list)):      
        for j in range(len(list)-1):            #  Bubble sort logic
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

if __name__ == '__main__':
    arr =[]
    n = int(input("Enter the number of elements: "))
    for i in range(0, n):               #  Taking input from user
        ele = int(input())
        arr.append(ele)         
    print("Unsorted list: ", arr)       #  Printing unsorted list

    print("Array before sorting: ", arr)
    print(bubble_sort(list))        #  Printing sorted list

