class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = collections.defaultdict(set) # r: set("1", "2", ...)
        col = collections.defaultdict(set) # c: set("1", "2", ...)      
        block = collections.defaultdict(set) # temp: set("1", "2", ...)
        unfilled = [] # unfilled cells
        
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    row[r].add(board[r][c]) # add num filled in each row
                    col[c].add(board[r][c]) # add num filled in each column
                    block[(r // 3, c // 3)].add(board[r][c]) # add num filled in each 3*3 block
                else:
                    unfilled.append((r, c)) # add unfilled cells
        
        def dfs():
            if len(unfilled) == 0: # finished if no more unfilled cells
                return True
            r, c = unfilled[-1] # get the last pair of (r, c) from unfilled
            temp = (r // 3, c // 3) # convert index 0 ~ 2 to 0, 3 ~ 5 to 1, 6 ~ 8 to 2
            for num in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                if num in row[r] or num in col[c] or num in block[temp]: # skip if num is already filled
                    continue
                
                # below are normal steps for backtracking
                board[r][c] = num
                row[r].add(num)
                col[c].add(num)
                block[temp].add(num)
                unfilled.pop()
                
                if dfs():
                    return True

                board[r][c] = "."
                row[r].remove(num)
                col[c].remove(num)
                block[temp].remove(num)
                unfilled.append((r, c))
            return False
        
        dfs()
