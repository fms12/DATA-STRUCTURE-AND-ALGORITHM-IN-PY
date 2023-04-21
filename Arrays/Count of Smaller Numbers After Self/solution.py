class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # get the length of the input array
        n = len(nums)
        
        # create an array of zeros with the same length as the input array
        counts = [0] * n
        
        # create an empty list to hold the sorted numbers
        sorted_nums = []
        
        # loop through the input array in reverse order
        for i in range(n - 1, -1, -1):
            # use the bisect_left function to find the index where the current number
            # should be inserted in the sorted list
            idx = bisect_left(sorted_nums, nums[i])
            
            # the number of elements to the right of the current index is equal to the
            # number of elements that are smaller than the current number
            counts[i] = idx
            
            # insert the current number into the sorted list at the correct index
            sorted_nums.insert(idx, nums[i])
        
        # return the array of counts
        return counts
