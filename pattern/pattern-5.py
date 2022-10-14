# Python program to print diamond star pattern

def pattern(n):
    # print upper triangle
    i = 1
    while i < n:
        # printing stars
        print(" "*(n-i) + "* " * i)
        i += 1

    # print lower triangle
    i = n
    while i >= 1:
        # printing stars
        print(" " * (n-i) + "* " * i)
        i -= 1


# calling function with 5 is input
pattern(5)

# skipcq
"""
Output
         *
        * *
    * * *
 * * * *
* * * * *
 * * * *
    * * *
        * *
         *
"""
