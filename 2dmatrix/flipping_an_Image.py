from typing import List


def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:
    for i in range(len(image)):
        # image[i] = image[i][::-1]
        # image[i].reverse()
        # image[i][0],image[i][len(image)-1]=image[i][len(image)-1],image[i][0]
        for j in range(len(image)):
            if(image[i][j] == 1):
                image[i][j] = 0
            else:
                image[i][j] = 1
    return image


# ###################################################################################################

# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
