def movesToChessboard(self, board: List[List[int]]) -> int:
    n = len(board)
    
    # check that there are half zeroes and half ones in the first row and column
    ones = sum(board[0])
    if ones != n//2 and ones != (n+1)//2:
        return -1
    ones = sum(board[i][0] for i in range(n))
    if ones != n//2 and ones != (n+1)//2:
        return -1
    
    # check that all the rows are either exactly the same as first or exactly inverted
    inv = 0
    for i in range(1,n):                
        if all(board[i][j] == board[0][j] for j in range(n)):
            pass
        elif all(board[i][j] != board[0][j] for j in range(n)):
            inv += 1
        else:
            return -1
            
    # the number of inversions should be half of n
    if inv != n//2 and inv != (n+1)//2:
        return -1
    
    # same for columns
    inv = 0
    for j in range(1,n):                
        if all(board[i][j] == board[i][0] for i in range(n)):
            pass
        elif all(board[i][j] != board[i][0] for i in range(n)):
            inv += 1
        else:
            return -1
        
    if inv != n//2 and inv != (n+1)//2:
        return -1
        
    # now we know the transformation is possible
    # count the difference from "01010..." in the first row and column
    diff_h = sum(1 for j in range(n) if board[0][j] == j%2)
    diff_v = sum(1 for i in range(n) if board[i][0] == i%2)
    if n%2:
        #for odd n: the right order is when diff is even
        return (diff_h if diff_h%2==0 else n-diff_h)//2 + \
               (diff_v if diff_v%2==0 else n-diff_v)//2
    else:
        #for even n: any order is fine
        return min(diff_h,n-diff_h)//2 + \
               min(diff_v,n-diff_v)//2
