from typing import List


class Solution:
    def busyStudent(
        self, startTime: List[int],
        endTime: List[int], queryTime: int
    ) -> int:
        n = len(startTime)
        count = 0
        for i in range(0, n):
            if (startTime[i] <= queryTime and endTime[i] >= queryTime):
                count = count+1
        return count


"""
OUTPUT:
Example 1:

Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
Output: 1
Explanation: We have 3 students where:
The first student started doing homework at time 1
and finished at time 3 and wasn't doing anything at time 4.
The second student started doing homework at time
2 and finished at time 2 and also wasn't doing anything at time 4.
The third student started doing homework at time 3
and finished at time 7 and was the only student doing homework at time 4.
"""
