def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        cout=0
        for i in range(len(arr)):
            for j in range(i,len(arr),2):
                    temp=arr[i:j+1]
                    cout+=sum(temp)
        return cout
        
   ###########################################################################
  
#  Input: arr = [1,4,2,5,3]
#  Output: 58
#  Explanation: The odd-length subarrays of arr and their sums are:
#  [1] = 1
#  [4] = 4
#  [2] = 2
#  [5] = 5
#  [3] = 3
#  [1,4,2] = 7
#  [4,2,5] = 11
#  [2,5,3] = 10
#  [1,4,2,5,3] = 15
#  If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
