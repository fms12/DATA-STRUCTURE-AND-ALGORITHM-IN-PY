def maxProduct(nums):
    first=0
    second=0
    for _, num in enumerate(nums):
        if (num > first):
            second = first
            first = num
        elif (num >= second):
            second = num
    print(first,second)


nums = [3,4,5,2]
maxProduct(nums)


###################################################
# OUTPUT

# (5,4)
