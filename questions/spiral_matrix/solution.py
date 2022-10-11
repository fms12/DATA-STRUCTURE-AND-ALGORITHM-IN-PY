"""
This program is a spiral matrix but it
spiral in the clock wise direction
"""


from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    res = []
    minr = 0
    minc = 0
    maxr = len(matrix)-1
    maxc = len(matrix[0])-1
    while (minr <= maxr and minc <= maxc):
        # top wall
        for j in range(minc, maxc+1):
            res.append(matrix[minr][j])
        minr += 1

        # right wall
        for i in range(minr, maxr+1):
            res.append(matrix[i][maxc])
        maxc -= 1

        # bottom wall
        if minr <= maxr and minc <= maxc:
            for j in range(maxc, minc-1, -1):
                res.append(matrix[maxr][j])
            maxr -= 1

            # left wall
            for i in range(maxr, minr-1, -1):
                res.append(matrix[i][minc])
            minc += 1

    return res



