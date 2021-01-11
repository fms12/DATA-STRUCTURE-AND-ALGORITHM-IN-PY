  def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        cout=0
        for i in range(len(arr)):
            for j in range(i,len(arr),2):
                    temp=arr[i:j+1]
                    cout+=sum(temp)
        return cout
        
leetcode question       
