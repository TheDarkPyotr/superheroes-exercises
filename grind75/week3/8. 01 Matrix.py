import math
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, col = len(mat), len(mat[0])
        output = [[-1 if mat[i][j] != 0 else 0 for j in range(col)] for i in range(rows)]

        queue = deque()
        visited = set()

        for i in range(rows):
            for j in range(col):
                if mat[i][j] == 0:
                    queue.append((i, j))

        distance = 0

        while len(queue) > 0:
            size = len(queue)

            while size > 0:
                size -= 1

                i, j = queue.popleft()

                if mat[i][j] != 0:
                    output[i][j] = distance

                #Quattro direzioni
                for i, j in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    #Controllo range righe/colonne e visitati
                    if 0 <= i < rows and 0 <= j < col and (i, j) not in visited:
                        visited.add((i, j))
                        queue.append((i, j))

            distance += 1

        return output
        
sol = Solution()
sol.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])