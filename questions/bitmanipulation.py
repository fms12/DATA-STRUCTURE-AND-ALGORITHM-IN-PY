#Consider bipartite graph of rows and columns. 
#If row and column intersection has 1, then connect with an edge corresponding vertices in the graph. 
#Swaping rows or columns correspond to swapping vertices in the graph. 
#At the end we want to have chessboard construction, which implies that we have connected component of odd rows connected to all odd columns or to all even columns.
#And all even rows connected to other half of columns. 
#So we will get two complete subgraphs which do not intersect with each other in our initial bipartite graph, and it is very intuitive that this is actually necessary and sufficient condition. 
#So after understanding whether you have two such complete subgraphs, it is easy to compute number of swaps required to move all rows and columns inside the same subgraph to odd or even indexes. Done.

from collections import defaultdict

class Solution:
    def movesToChessboard(self, board):
        n = len(board)
        gr = defaultdict(set)

        for i in range(n):
            for j in range(n):
                if board[i][j]:
                    gr[i].add(j + 2 * n)
                    gr[j + 2 * n].add(i)

        def assign(base = 0):
            len_base, deg = len(gr[base]), n // 2
            if n % 2 == 0 and len_base != deg: return -1
            if n % 2 == 1 and not (0 <= len_base - deg <= 1): return -1

            first = {base}
            second = set()

            for j in range(base, base + n):
                intersection = gr[base] & gr[j]
                if len(intersection) == 0 and len(gr[j]) == n - len_base:
                    second.add(j)
                elif len(intersection) == len_base and len(gr[j]) == len_base:
                    first.add(j)
                else:
                    return -1

            v1, v2 = sum(f % 2 for f in first), sum((f + 1) % 2 for f in first)

            if n % 2 == 1:
                return v2 if len(first) == deg else v1

            return min(v1, v2)

        v1, v2 = assign(), assign(2 * n)
        if v1 == -1 or v2 == -1: return -1
        return v1 + v2
