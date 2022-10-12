# Python3 program to find 4 elements
# with given sum

# The following structure is needed
# to store pair sums in aux[]


class pairSum:

	def __init__(self):
		# Index (int A[]) of first element in pair
		self.first = ""

		# Index of second element in pair
		self.sec = ""

		# Sum of the pair
		self.sum = ""


# Function to check if two given pairs
# have any common element or not
def noCommon(a, b):
	if (a.first == b.first or a.first == b.sec or a.sec == b.first or a.sec == b.sec):
		return False

	return True


# The function finds four
# elements with given sum X
def findFourElements(myArr, sum):

	length = len(myArr)

	# Create an auxiliary array to
	# store all pair sums
	size = ((length * (length - 1)) // 2)
	aux = [None for _ in range(size)]

	# Generate all possible pairs
	# from A[] and store sums
	# of all possible pairs in aux[]
	k = 0
	for i in range(length - 1):
		for j in range(i + 1, length):
			aux[k] = pairSum()
			aux[k].sum = myArr[i] + myArr[j]
			aux[k].first = i
			aux[k].sec = j
			k += 1

	# Sort the aux[] array using
	# library function for sorting
	aux.sort(key=lambda x: x.sum)

	# Now start two index variables
	# from two corners of array
	# and move them toward each other.
	i = 0
	j = size - 1
	while (i < size and j >= 0):
		if ((aux[i].sum + aux[j].sum == sum)
				and noCommon(aux[i], aux[j])):
			print(myArr[aux[i].first], myArr[aux[i].sec],
				myArr[aux[j].first], myArr[aux[j].sec], sep=", ")
			return

		elif (aux[i].sum + aux[j].sum < sum):
			i += 1
		else:
			j -= 1


# Driver Code
arr = [10, 20, 30, 40, 1, 2]
X = 91

# Function call
findFourElements(arr, X)

