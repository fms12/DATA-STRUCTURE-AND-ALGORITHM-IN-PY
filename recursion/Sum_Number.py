# Sum of digits (recursive)

# Write a recursive function that returns the sum of the digits of a given integer.
# Input format :
# Integer N
# Output format :
# Sum of digits of N
# Constraints :
# 0 <= N <= 10^9
# Sample Input 1 :
# 12345
# Sample Output 1 :
# 15
# Sample Input 2 :
# 9
# Sample Output 2 :
# 9


def sumnumber(a):
    if(a<10):
        return a
    sums = a%10 + sumnumber(a//10)
    return sums

a = int(input())
print(sumnumber(a))
