# Python code to find number of unique paths
# in a Matrix
def  UniquePathHelper(i, j, r, c, A):
   
    # boundary condition or constraints
    if(i == r or j == c):
      return 0
     
    if(A[i][j] == 1):
      return 0
     
    # base case
    if(i == r-1 and j == c-1):
      return 1
 
    return  UniquePathHelper(i+1, j, r, c, A) + UniquePathHelper(i, j+1, r, c, A)
 
def uniquePathsWithObstacles(A):
    r,c = len(A),len(A[0])
     
    return UniquePathHelper(0, 0, r, c, A)
 
# Driver code
A = [ [ 0, 0, 0 ],
      [ 0, 1, 0 ],
      [ 0, 0, 0 ] ]
                              
print(uniquePathsWithObstacles(A))   
