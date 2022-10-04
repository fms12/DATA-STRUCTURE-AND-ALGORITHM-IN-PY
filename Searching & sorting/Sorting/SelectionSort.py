//                                      SELECTION SORT

//The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) 
//from the unsorted part and putting it at the beginning. 

//The algorithm maintains two subarrays in a given array.

//The subarray which already sorted. 
//The remaining subarray was unsorted.
//In every iteration of the selection sort, the minimum element (considering ascending order) 
//from the unsorted subarray is picked and moved to the sorted subarray. 

# Python program for implementation of Selection
# Sort
import sys
A = [64, 25, 12, 22, 11]

# Traverse through all array elements
for i in range(len(A)):
	
	# Find the minimum element in remaining
	# unsorted array
	min_idx = i
	for j in range(i+1, len(A)):
		if A[min_idx] > A[j]:
			min_idx = j
			
	# Swap the found minimum element with
	# the first element	
	A[i], A[min_idx] = A[min_idx], A[i]

# Driver code to test above
print ("Sorted array")
for i in range(len(A)):
	print("%d" %A[i],end=" ")


//Time Complexity: The time complexity of Selection Sort is O(N2)

//Auxiliary Space: O(1) as the only extra memory used is for temporary variables while swapping two values in Array. 
//The selection sort never makes more than O(N) swaps and can be useful when memory write is a costly operation. 
