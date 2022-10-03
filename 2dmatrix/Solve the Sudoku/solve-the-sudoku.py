#User function Template for python3
import copy
class Solution:
    def __init__(self):
        self.ans=[]
    #Function to find a solved Sudoku.
    grid=[]
    def SolveSudoku(self,grid):
        def valid(grid,p,x,y):
            for i in range(9):
                if(p in (grid[x][i], grid[i][y])):
                    return 0
            s=3*(x//3)
            e=3*(y//3)
            for i in range(s,s+3):
                for j in range(e,e+3):
                    if(grid[i][j]==p):
                        return 0
            return 1
        def end():
            for i in range(9):
                for j in range(9):
                    if(grid[i][j]==0):
                        return [i,j]
            return 1
        def solve():
            x=end()
            if(x==1):
                self.ans=copy.deepcopy(grid)
                return
            for p in range(1,10):
                if(valid(grid,p,x[0],x[1])):
                    grid[x[0]][x[1]]=p
                    solve()
                    grid[x[0]][x[1]]=0
        solve()
        grid=copy.deepcopy(self.ans)
        if(self.ans):
            return 1
        return 0
    def call(self):
        return self.ans
    #Function to print grids of the Sudoku.  
    def printGrid(self):
        grid=self.call()
        for i in grid:
            print(*i,end=" ")
        # Your code here
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
                
        ob = Solution()
            
        if(ob.SolveSudoku(grid) is True):
            ob.printGrid(grid)
            print()
        else:
            print("No solution exists")
        t = t-1
# } Driver Code Ends