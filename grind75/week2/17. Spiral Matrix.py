class Solution:
    def spiralOrder(self, matrix):
        
        m = len(matrix) #Numero di righe
        n = len(matrix[0]) #Numero di colonne

        left = 0        #Deliminatore sx colonna
        right = n-1     #Deliminatore dx colonna
        top = 0         #Deliminatore min riga
        bottom = m - 1  #Delimitatore max riga
        res = []

        while left <= right and top <= bottom:
        
            for col in range(left, right+1): #Prima riga
                res.append(matrix[top][col])
            top += 1

            for row in range(top, bottom+1): #Ultima colonna
                res.append(matrix[row][right])
            right -= 1

            for col in range(right, left-1, -1): #Ultima riga (dalla fine)
                res.append(matrix[bottom][col])
            bottom -= 1

            for row in range(bottom, top-1, -1): #Prima Colonna (dal basso)
                res.append(matrix[row][left])
            left += 1

        #Elimino elementi ridondanti
        return res[:m*n]


solution = Solution()
#solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
#solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
a = solution.spiralOrder([[1,2,3,4,5,6,7,8,9,10,11,12],[13,14,15,16,17,18,19,20,21,22,23,24],[25,26,27,28,29,30,31,32,33,34,35,36],[1,2,3,4,5,6,7,8,9,10,11,12],[13,14,15,16,17,18,19,20,21,22,23,24],[25,26,27,28,29,30,31,32,33,34,35,36]])
print(a)
#[[1,2,3,4,5,6,7,8,9,10,11,12],[13,14,15,16,17,18,19,20,21,22,23,24],[25,26,27,28,29,30,31,32,33,34,35,36]]
            
"""

[[".",".",".",".",".",".","5",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,["9","3",".",".","2",".","4",".","."]
,[".",".","7",".",".",".","3",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".","3","4",".",".",".","."]
,[".",".",".",".",".","3",".",".","."]
,[".",".",".",".",".","5","2",".","."]]

"""
            
        