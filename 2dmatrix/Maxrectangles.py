# Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.
# Python3 program for the above approach
from bisect import bisect_left, bisect_right
import sys

# Function to find the maximum possible
# sum of arectangle which is less than K
def maxSubarraySum(sum, k, row):

	curSum, curMax = 0, -sys.maxsize - 1

	# Stores the values (cum_sum - K)
	sumSet = {}

	# Insert 0 into the set sumSet
	sumSet[0] = 1

	# Traverse over the rows
	for r in range(row):
		
		# Get cumulative sum from [0 to i]
		curSum += sum[r]

		# Search for upperbound of
		# (cSum - K) in the hashmap
		arr = list(sumSet.keys())

		it = bisect_left(arr, curSum - k)

		# If upper_bound of (cSum - K)
		# exists, then update max sum
		if (it != len(arr)):
			curMax = max(curMax, curSum - it)

		# Insert cumulative value
		# in the hashmap
		sumSet[curSum] = 1

	# Return the maximum sum
	# which is less than K
	return curMax

# Function to find the maximum sum of
# rectangle such that its sum is no
# larger than K
def maxSumSubmatrix(matrix, k):
	
	# Stores the number of rows
	# and columns
	row = len(matrix)
	col = len(matrix[0])

	# Store the required result
	ret = -sys.maxsize - 1

	# Set the left column
	for i in range(col):
		sum = [0] * (row)

		# Set the right column for the
		# left column set by outer loop
		for j in range(i, col):
			
			# Calculate sum between the
			# current left and right
			# for every row
			for r in range(row):
				sum[r] += matrix[r][j]

			# Stores the sum of rectangle
			curMax = maxSubarraySum(sum, k, row)

			# Update the overall maximum sum
			ret = max(ret, curMax)

	# Print the result
	print(ret)

	
matrix = [ [ 1, 0, 1 ], [ 0, -2, 3 ] ]
K = 2
maxSumSubmatrix(matrix, K)
