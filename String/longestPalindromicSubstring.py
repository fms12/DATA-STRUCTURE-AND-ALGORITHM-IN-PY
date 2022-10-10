# A Python3 solution for longest palindrome

# Function to pra subString s[low..high]
def printSubStr(s, low, high):
	
	for i in range(low, high + 1):
		print(s[i], end = "")

# This function prints the
# longest palindrome subString
# It also returns the length
# of the longest palindrome
def longestPalSubstr(s):
	
	# Get length of input String
	n = len(s)
	
	# All subStrings of length 1
	# are palindromes
	maxLength = 1
	start = 0
	
	# Nested loop to mark start
	# and end index
	for i in range(n):
		for j in range(i, n):
			flag = 1
			
			# Check palindrome
			for k in range(0, ((j - i) // 2) + 1):
				if (s[i + k] != s[j - k]):
					flag = 0

			# Palindrome
			if (flag != 0 and (j - i + 1) > maxLength):
				start = i
				maxLength = j - i + 1
				
	print("Longest palindrome subString is: ", end = "")
	printSubStr(s, start, start + maxLength - 1)

	# Return length of LPS
	return maxLength

# Driver Code
if __name__ == '__main__':

	s = "banana"
	
	print("\nLength is: ", longestPalSubstr(s))
