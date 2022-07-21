class Solution:
    def isValidSudoku(self, board) -> bool:
        
        row_dict = {}
        col_dict = {}
        
        n = len(board)      #Numero righe
        m = len(board[0])   #Numero colonne
        top = 0
        bottom = n-1
        left = 0
        right = m-1
        
        for i in range(0,9):
            row_dict.clear()
            col_dict.clear()
            for j in range(0,9):
                
                if board[i][j] != ".":
                    row_dict[board[i][j]] = 1 + row_dict.get(board[i][j],0)
                    if  row_dict[board[i][j]] > 1:
                        return False
                    
                if board[j][i] != ".":
                    col_dict[board[j][i]] = 1 + col_dict.get(board[j][i],0)
                    if col_dict[board[j][i]] > 1:
                        return False
            #if len(row_dict) == 0 or len(col_dict) == 0:
            #    return False
            
        row_dict.clear()        
        while top <= bottom:
            
            while left <= right:
                for col in range(3):
                    print("########################################################################à")
                    for row in range(3):
                        
                        print("matrix[{}][{}] = {}".format(top+col,left+row,board[top+col][left+row]))
                        if board[top+col][left+row].isnumeric():
                            row_dict[board[top+col][left+row]] = 1 + row_dict.get(board[top+col][left+row],0)
                            if row_dict[board[top+col][left+row]] > 1:
                                print("DUPLICATE matrix[{}][{}] = {}".format(top+col,left+row,board[top+col][left+row]))
                                #print("top {} left {}".format(top,left))
                                return False        
                left += 3
                row_dict = {}
            top += 3

       
        return True

sol = Solution()
#sol.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
sol.isValidSudoku([[".",".",".",".",".",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],["9","3",".",".","2",".","4",".","."],[".",".","7",".",".",".","3",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".","3","4",".",".",".","."],[".",".",".",".",".","3",".",".","."],[".",".",".",".",".","5","2",".","."]]
)