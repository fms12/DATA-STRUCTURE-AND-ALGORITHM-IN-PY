# Merge Sort is a Divide and Conquer algorithm. 
# It divides input array in two halves,
# calls itself for the two halves and then merges the two sorted halves

def merge(arr, l, m, r):
	# Merges two subarrays
	n1 = m - l + 1
	n2 = r - m

	# create temp arrays
	L = [0] * (n1)
	R = [0] * (n2)

# Adding elements to the left part
	for i in range(0, n1):
		L[i] = arr[l + i]

# Adding elements to the right part
	for j in range(0, n2):
		R[j] = arr[m + 1 + j]
	i = 0
	j = 0
	k = l

# Sorting and adding elements to the array from both the half
	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

# Sorts the passed array
def mergeSort2(arr, l, r):
	if l < r:

		m = l+(r-l)//2
		mergeSort2(arr, l, m)
		mergeSort2(arr, m+1, r)
		merge(arr, l, m, r)

# Function to return a sorted array.
def mergeSort(L):
    arr=L
    mergeSort2(arr,0,len(arr)-1)
    return arr

# Sample Case
print(mergeSort([2,4,9,1,2,7,32,3]))