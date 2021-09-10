# Count Zeros

# Given an integer N, count and return the number of zeros that are present in the given integer using recursion.
# Input Format :
# Integer N
# Output Format :
# Number of zeros in N
# Constraints :
# 0 <= N <= 10^9
# Sample Input 1 :
# 10204
# Sample Output 1 :
# 2
# Sample Input 2 :
# 708000
# Sample Output 2 :
# 4



def zero(a):
    if(a<10):
        if(a==0):
            return 1
        else:
            return 0
    if(a%10==0):
        return zero(a//10) + 1
    else:
        return zero(a//10)

a = int(input())
print(zero(a))
