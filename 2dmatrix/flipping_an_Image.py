from typing import List


def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:
    for _, val in enumerate(image):
        for j in range(len(image)):
            if(val[j] == 1):
                val[j] = 0
            else:
                val[j] = 1
    return image


# ###################################################################################################

# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
