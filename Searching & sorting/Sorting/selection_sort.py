# The selection sort algorithm sorts an array by repeatedly finding the minimum element.
# Time Complexity :  O(n*n)

"""
Algorithm :-

Step 1 − Set MIN to location 0
Step 2 − Search the minimum element in the list
Step 3 − Swap with value at location MIN
Step 4 − Increment MIN to point to next element
Step 5 − Repeat until list is sorted

Pseudocode Selection Sort  :-

   list  : array of items
   n     : size of list

   for i = 1 to n - 1
   /* set current element as minimum*/
      min = i    
  
      /* check the element to be minimum */

      for j = i+1 to n 
         if list[j] < list[min] then
            min = j;
         end if
      end for

      /* swap the minimum element with the current element*/
      if indexMin != i  then
         swap list[min] and list[i]
      end if
   end for
    
end procedure
"""


# define a fuction
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:  # Selection sort logic
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


if __name__ == "__main__":
    arr = []  # empty list
    n = int(input("Enter the number of elements: "))
    for i in range(0, n):  # Taking input from user
        ele = int(input())
        arr.append(ele)
    print("Unsorted list: ", arr)

    print("Array before sorting: ", arr)  # Printing unsorted list
    print(selection_sort(list))
