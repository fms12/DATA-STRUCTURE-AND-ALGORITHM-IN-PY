class Solution:
   def solve(self, matrix):
      if not matrix or not matrix[0]:
         return []
      n = len(matrix)
      for row in matrix:
         row.reverse()
      for i in range(n):
         for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i],
            matrix[i][j]
      return matrix
ob = Solution()
matrix = [
[1, 4, 7],
[2, 5, 8],
[3, 6, 9]
]
print(ob.solve(matrix))
