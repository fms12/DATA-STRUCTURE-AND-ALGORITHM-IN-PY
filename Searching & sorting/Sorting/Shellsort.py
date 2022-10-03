# Algorithm
# 1)Initialize h(h=size)
# 2)Divide the list into sublists each of interval h
# 3)Now, use insertion sort to sort these sublists
# 4)Repeat the above steps need to be until the list is completely sorted


#Implementation of Shell Sort
import math
def shellSort(arr):

	# Start with a big gap, then reduce the gap
	n = len(arr)
	gap =math.floor(n/2)

	# Do a gapped insertion sort for this gap size.
	# The first gap elements a[0..gap-1] are already in gapped
	# order keep adding one more element until the entire array
	# is gap sorted
	while gap > 0:
		for i in range(gap,n):
			# add a[i] to the elements that have been gap sorted
			# save a[i] in temp and make a hole at position i
			temp = arr[i]

			# shift earlier gap-sorted elements up until the correct
			# location for a[i] is found
			j = i
			while j >= gap and arr[j-gap] >temp:
				arr[j] = arr[j-gap]
				j -= gap

			# put temp (the original a[i]) in its correct location
			arr[j] = temp
		gap= math.floor(gap/2)


arr = [ 12, 34, 54, 2, 3, 8]
n = len(arr)
print ("Array before sorting:")
for i in range(n):
	print(arr[i])
shellSort(arr)
print ("\nArray after sorting:")
for i in range(n):
	print(arr[i])
