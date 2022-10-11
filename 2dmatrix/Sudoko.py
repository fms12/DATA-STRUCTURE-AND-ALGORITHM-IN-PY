class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
		
		
		#the method curr_posn will return the Current position we are dealing with the board. 
		#it simply returns the Position of first '.' in the board
        def curr_posn(arr):
            for i in range(0,9):
                for j in range(0,9):
                    if arr[i][j]=='.':
                        return (i,j)
            return (-1,-1)
        
		# the method comp will tell us whether we have completed the sudoku or not
		def comp(arr):
            for i in range(0,9):
                for j in range(0,9):
                    if arr[i][j]=='.':
                        return False
            return True
        
		
		# the method choice will give us a list of all choices that we can place in the position (x,y)
		def choice(arr,x,y):
			# we take all Numbers from one to 9 in ans array and remove elements in the ans array if they are in the grid or row or column we are dealing with
            ans=[1,2,3,4,5,6,7,8,9]
			#this loop is for 3X3 grid which contains (x,y)
            for i in range(3*(x//3),3*(x//3+1)):
                for j in range(3*(y//3),3*(y//3+1)):
                    if arr[i][j]!='.' and int(arr[i][j]) in ans:
                        ans.remove(int(arr[i][j]))
					
			# this loop is For the row we are currently dealing with
            for i in range(0,9):
                if arr[x][i]!='.' and int(arr[x][i]) in ans:
                    ans.remove(int(arr[x][i]))
			# this loop is for the column we are currently dealing with
            for i in range(0,9):
                if arr[i][y]!='.' and int(arr[i][y]) in ans:
                    ans.remove(int(arr[i][y]))
            return ans
        
		#we introduced c to not to make solve again and again after completing it
		c=0
        board=board
        
		#this is our main algo
		def solve(arr):
            nonlocal c
            if c==1:
                return
            if comp(arr):
                c+=1
                nonlocal board
                for i in range(0,9):
                    for j in range(0,9):
                        board[i][j]=arr[i][j]
                return arr
            else:
                q=curr_posn(arr)
                for i in choice(arr,q[0],q[1]):
                    a=copy.deepcopy(arr)
                    a[q[0]][q[1]]=str(i)
                    solve(a)
        solve(board)
