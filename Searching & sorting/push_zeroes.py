# Given list
arr = [5, 6, 0, 4, 6, 0, 9, 0, 8]
 
# Storing all non zero values
nonZeroValues = [x for x in arr if x != 0]
 
# Storing all zeroes
zeroes = [j for j in arr if j == 0]
 
# Updating the answer
arr = nonZeroValues + zeroes
 
# Printing the answer
print( "array after shifting zeros to right side: " + arr)
