def maxProduct(nums):        
        first=0
        second=0
        for i in range(len(nums)):
            if (nums[i] > first):
                second = first
                first = nums[i]
            elif (nums[i] >= second):
                second = nums[i]
        print(first,second)
nums = [3,4,5,2]
maxProduct(nums)
###################################################
#OUTPUT

#(5,4)
