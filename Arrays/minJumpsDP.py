# Returns minimum number of jumps
# to reach arr[n-1] from first position (0-indexed)


def minJumps(arr, n):
	jumps = [0 for i in range(n)]
  
  	#if first element is 0 or size of array
  	#is zero
	
  	if n == 0 or arr[0] == 0:
		return float('inf')

	jumps[0] = 0

	# Find the minimum number of
	# jumps to reach arr[i] from
	# arr[0] and assign this
	# value to jumps[i]
	
  
  	for i in range(1, n):
		jumps[i] = float('inf')
		for j in range(i):
			if i <= j + arr[j] and jumps[j] != float('inf'):
				jumps[i] = min(jumps[i], jumps[j] + 1)
				break
	return jumps[n-1]

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
size = len(arr)
print(f'Minimum number of jumps to reach end is {minJumps(arr, size)}' )
