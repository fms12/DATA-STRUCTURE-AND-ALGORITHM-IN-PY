# Bubble sort
# define a fuction
def bubble_sort(listt):      
    for _ in range(len(listt)):      
        for j in range(len(listt)-1):            #  Bubble sort logic
            if listt[j] > listt[j+1]:
                listt[j], listt[j+1] = listt[j+1], listt[j]
    return listt

if __name__ == '__main__':
    arr =[]
    n = int(input("Enter the number of elements: "))
    for i in range(0, n):               #  Taking input from user
        ele = int(input())
        arr.append(ele)         
    print("Unsorted list: ", arr)       #  Printing unsorted list

    print("Array before sorting: ", arr)
    print(bubble_sort(arr))        #  Printing sorted list

